#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import base64
import json
from torch.utils import data
from torch.nn import functional as F
pd.set_option('display.max_columns',300)
import random
from tqdm import tqdm
import pickle
import torch
from torch import nn, optim
from torch.utils.data import Dataset, Subset, DataLoader
import os
os.environ['CUDA_VISIBLE_DEVICES']='3,4,5'
from transformers import *
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", do_lower_case=True)
import time


# In[2]:


train = pd.read_csv('../data_0407/train.tsv',sep='\t',nrows=1000000,quoting=3)
valid = pd.read_csv('../data_0407/valid.tsv',sep='\t',quoting=3)
test = pd.read_csv('../data_0407/testA.tsv',sep='\t',quoting=3)


# In[3]:


def decode_rows(row):
    row['boxes'] = np.frombuffer(base64.b64decode(row['boxes']), dtype=np.float32).reshape(row['num_boxes'], 4)
    row['features'] = np.frombuffer(base64.b64decode(row['features']), dtype=np.float32).reshape(row['num_boxes'], 2048)
    row['class_labels'] = np.frombuffer(base64.b64decode(row['class_labels']), dtype=np.int64).reshape(row['num_boxes'])
    return row
train = train.apply(lambda x: decode_rows(x), axis=1)
valid = valid.apply(lambda x: decode_rows(x), axis=1)
test = test.apply(lambda x: decode_rows(x), axis=1)


# In[4]:


with open("../data_0407/valid_answer.json",'r') as load_f:
    load_dict = json.load(load_f)
def get_target(row):
    row['target'] = int(row['product_id'] in load_dict[str(row['query_id'])])
    return row
valid = valid.apply(lambda x:get_target(x),axis=1)


# In[5]:


def find_max_boxes(x):
    max_index = -1
    max_box = 0
    count = 0
    for i in x:
        if (i[2]-i[0])*(i[3]-i[1])>max_box:
            max_index=count
            max_box = (i[2]-i[0])*(i[3]-i[1])
        count = count + 1
    return max_index
train['boxes_max'] = train['boxes'].apply(find_max_boxes)
valid['boxes_max'] = valid['boxes'].apply(find_max_boxes)
test['boxes_max'] = test['boxes'].apply(find_max_boxes)


# In[6]:


def find_max_boxes_embed(index,feature):
    return feature[index]
train['max_boxes_embed'] = train.apply(lambda rows:find_max_boxes_embed(rows['boxes_max'],rows['features']),axis=1)
valid['max_boxes_embed'] = valid.apply(lambda rows:find_max_boxes_embed(rows['boxes_max'],rows['features']),axis=1)
test['max_boxes_embed'] = test.apply(lambda rows:find_max_boxes_embed(rows['boxes_max'],rows['features']),axis=1)


# In[7]:


def preprocess(data):
    punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~`" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
    def clean_special_chars(text, punct):
        for p in punct:
            text = text.replace(p, ' ')
        return text.lower()
    
    remove_words=['and','of']
    def remove_word(text,remove_words):
        text_temp = [i for i in text.split(' ') if i not in remove_words]
        return ' '.join(text_temp)
    
    data = data.astype(str).apply(lambda x: clean_special_chars(x, punct))
    data = data.astype(str).apply(lambda x: remove_word(x, remove_words))
    return data

train['query_pre'] = preprocess(train['query'])
valid['query_pre'] = preprocess(valid['query'])
test['query_pre'] = preprocess(test['query'])




def convert_data_apply(text, max_seq_length=300,tokenizer=None):
    one_token = tokenizer.encode(text,add_special_tokens=True, max_length=max_seq_length,pad_to_max_length=max_seq_length)
    return one_token





train['bert_token'] = train['query_pre'].apply(lambda x:convert_data_apply(x,10,tokenizer))
valid['bert_token'] = valid['query_pre'].apply(lambda x:convert_data_apply(x,10,tokenizer))
test['bert_token'] = test['query_pre'].apply(lambda x:convert_data_apply(x,10,tokenizer))



train.to_pickle('train_temp_data.pkl',protocol=4)
#train = pd.read_pickle('train_temp_data.pkl')


# # negative_sampling

# In[16]:


test['item'] = test['query'].apply(lambda x:x.split(' ')[-1])
valid['item'] = valid['query'].apply(lambda x:x.split(' ')[-1])

item_leak = test['item'].drop_duplicates().values.tolist() + valid['item'].drop_duplicates().values.tolist()

train['item'] = train['query'].apply(lambda x:x.split(' ')[-1])

train = train[train['item'].isin(item_leak)]

train_sample = train.groupby('item')['product_id'].apply(list)

train_true = (train['query_id'].astype('str')+'_'+train['product_id'].astype('str')).values


train_neg_sample = train[['query_id','item']].values

from multiprocessing import cpu_count,Pool
'多进程处理'
def pool_extract(data, f,chunk_size,train_true,train_sample, worker=4):
    cpu_worker = cpu_count()
    print('cpu core:{}'.format(cpu_worker))
    if worker == -1 or worker > cpu_worker:
        worker = cpu_worker
    print('use cpu:{}'.format(worker))
    t1 = time.time()
    len_data = len(data)
    start = 0
    end = 0
    p = Pool(worker)
    res = []  # 保存的每个进程的返回值
    while end < len_data:
        end = start + chunk_size
        if end > len_data:
            end = len_data
        rslt = p.apply_async(f, (data[start:end],train_true,train_sample))
        start = end
        res.append(rslt)
    p.close()
    p.join()
    t2 = time.time()
    print((t2 - t1)/60)
    results = pd.concat([i.get() for i in res], axis=0, ignore_index=True)
    return results

def neg_sample_f(train_neg_sample,train_true,train_sample):
    neg_sample = []
    for i in tqdm(train_neg_sample,disable=False):
        product_id_sample = random.sample(train_sample[i[1]],1)[0]
        count = 0
        while (str(i[0])+'_'+str(product_id_sample) in train_true) and (count<=5):
            product_id_sample = random.sample(train_sample[i[1]],1)[0]
            count = count+1
        if count!=5:
            neg_sample.append([i[0],product_id_sample])
    return pd.DataFrame(neg_sample,columns=['query_id','product_id'])

train_neg_sample_df = pool_extract(train_neg_sample, neg_sample_f,10000,train_true,train_sample, worker=30)

neg_sample_df = train_neg_sample_df
neg_sample_df = pd.merge(neg_sample_df,train[['query_id','bert_token']],how='left')
neg_sample_df = pd.merge(neg_sample_df,train[['product_id','max_boxes_embed']],how='left')

neg_sample_df.to_pickle('train_negtive.pkl',protocol=4)


#neg_sample_df = pd.read_pickle('train_negtive.pkl')




train['target'] = 1
neg_sample_df['target']=0
train_data = pd.concat([train[['query_id', 'product_id', 'bert_token', 'max_boxes_embed','target']]
                        ,neg_sample_df]).sample(frac=1)

import gc
del train,neg_sample_df
gc.collect()

train_data.to_pickle('train_all.pkl',protocol=4)
#train_data = pd.read_pickle('train_all.pkl')




class MyDataset(Dataset):
    def __init__(self, data1,data2,labels):
        self.data1 = data1
        self.data2 = data2
        self.labels = labels  # 我的例子中label是一样的，如果你的不同，再增加一个即可

    def __getitem__(self, index):    
        img1, query,target = self.data1[index], self.data2[index], self.labels[index]
        return img1,query,target

    def __len__(self):
        return len(self.data1) # 我的例子中len(self.data1) = len(self.data2)
    
class MyDataset_test(Dataset):
    def __init__(self, data1,data2):
        self.data1 = data1
        self.data2 = data2

    def __getitem__(self, index):    
        img1, query = self.data1[index], self.data2[index]
        return img1,query

    def __len__(self):
        return len(self.data1) # 我的例子中len(self.data1) = len(self.data2)




test_picture_torch = torch.tensor(test['max_boxes_embed'].values.tolist(), dtype=torch.float32)
test_word_torch = torch.tensor(test['bert_token'].values.tolist(), dtype=torch.long)
test_torch_dataset = MyDataset_test(test_picture_torch,test_word_torch)




valid_picture_torch = torch.tensor(valid['max_boxes_embed'].values.tolist(), dtype=torch.float32)
valid_word_torch = torch.tensor(valid['bert_token'].values.tolist(), dtype=torch.long)
valid_y = torch.tensor(valid['target'].values,dtype=torch.float32)
valid_torch_dataset = MyDataset(valid_picture_torch,valid_word_torch,valid_y)


# In[23]:


train_picture_torch = torch.tensor(train_data['max_boxes_embed'].values.tolist(), dtype=torch.float32)
pickle.dump(train_picture_torch,open('torch_train_picture.pkl','wb'),protocol=4)
train_word_torch = torch.tensor(train_data['bert_token'].values.tolist(), dtype=torch.long)
pickle.dump(train_word_torch,open('torch_train_word.pkl','wb'),protocol=4)
train_y = torch.tensor(train_data['target'].values,dtype=torch.float32)
pickle.dump(train_y,open('torch_train_label.pkl','wb'),protocol=4)

# train_picture_torch = pickle.load(open('torch_train_picture.pkl','rb'))
# train_word_torch = pickle.load(open('torch_train_word.pkl','rb'))
# train_y = pickle.load(open('torch_train_label.pkl','rb'))

train_torch_dataset = MyDataset(train_picture_torch,train_word_torch,train_y)


def valid_score(oof,valid_y):
    oof['prob'] = valid_y
    oof = oof.sort_values('prob',ascending=False)
    sub1 = oof.groupby('query_id')['product_id'].apply(list).apply(lambda x:x[0])
    sub2 = oof.groupby('query_id')['product_id'].apply(list).apply(lambda x:x[1])
    sub3 = oof.groupby('query_id')['product_id'].apply(list).apply(lambda x:x[2])
    sub4 = oof.groupby('query_id')['product_id'].apply(list).apply(lambda x:x[3])
    sub5 = oof.groupby('query_id')['product_id'].apply(list).apply(lambda x:x[4])
    oof_sub = pd.concat([sub1,sub2,sub3,sub4,sub5],axis=1).reset_index()
    sub_example = pd.read_csv('../data_0407/submission.csv')
    oof_sub.columns= sub_example.columns
    ###
    ### 线下得分
    def get_score_for_ndcg(row):
        row['score_list'] = []
        for i in range(1,6):
            if row[f'product{i}'] in load_dict[str(row['query-id'])]:
                row['score_list'].append(1)
            else:
                row['score_list'].append(0)
        return row
    oof_sub = oof_sub.apply(lambda x:get_score_for_ndcg(x),axis=1)
    ### oof_input and golden_list
    oof_input = oof_sub['score_list'].tolist()
    golden_list = []
    for i in list(load_dict.keys()):
        if len(load_dict[i])>=5:
            golden_list.append([1]*5)
        else:
            golden_list.append([1]*len(load_dict[i])+[0]*(5-len(load_dict[i])))
    # compute dcg@k for a single sample
    def dcg_at_k(r, k):
        r = np.asfarray(r)[:k]
        if r.size:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(3, r.size + 2)))
        return 0.


    # compute ndcg@k (dcg@k / idcg@k) for a single sample
    def get_ndcg(r, ref, k):
        dcg_max = dcg_at_k(ref, k)
        if not dcg_max:
            return 0.
        dcg = dcg_at_k(r, k)
        return dcg / dcg_max
    final_score = 0
    for s1,s2 in zip(oof_input,golden_list):
        final_score+=get_ndcg(s1,s2,5)
    print('validation set ndcg score:',final_score/len(oof_input))
    return final_score/len(oof_input)


# In[27]:


class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.linear_picture = nn.Linear(2048, 100)
        self.linear_word = nn.Linear(768,100)        
        self.out_linear = nn.Linear(200,1)     

    def forward(self, picture, word):
        picture_embedding = self.linear_picture(picture)
        word_bert = self.bert(word)[0][:,0,:]
        word_embedding = F.relu(self.linear_word(word_bert))
        out = torch.sigmoid(self.out_linear(torch.cat([word_embedding,picture_embedding],1)))
        #out = torch.cosine_similarity(picture_embedding,word_embedding,dim=1).unsqueeze(dim=1)
        #print (picture_embedding)
        #out = torch.sigmoid(torch.sum(torch.matmul(picture_embedding,word_embedding.t()),dim=1).unsqueeze(dim=1))
        
        return out
    
def get_model_optimizer():
    model = NeuralNet()
    model.cuda()
    model = nn.DataParallel(model)
    params = list(model.named_parameters())

    def is_backbone(n):
        return "bert" in n

    optimizer_grouped_parameters = [
        {'params': [p for n, p in params if not is_backbone(n)],
         'lr': 5e-5 * 500}
    ]

    optimizer = AdamW(optimizer_grouped_parameters, lr=5e-4)

    return model, optimizer


# In[28]:


batch_size = 2048+512
n_epochs=15
loss_fn = torch.nn.BCELoss()
from sklearn.metrics import mean_squared_error
early_stopping_mode = 'max'


# In[ ]:


result_dev_pred = []
import time
n_flods = 5
model_prefix='baseline'

    
total_batch = round((len(train_picture_torch)/batch_size)+0.5)
total_batch_valid = round((len(valid_word_torch)/batch_size)+0.5)
total_batch_test = round((len(test_word_torch)/batch_size)+0.5)
model, optimizer = get_model_optimizer()

total_steps = (len(train_picture_torch)/n_epochs/batch_size )
scheduler = get_linear_schedule_with_warmup(optimizer, 
                                            num_warmup_steps=100,
                                            num_training_steps=total_steps)


# In[ ]:


for epoch in range(n_epochs):
    ###################train data###################
    train_index = [i for i in range(len(train_picture_torch))]
    random.shuffle(train_index)
    data_train = train_torch_dataset[train_index]
    data_train = MyDataset(data_train[0],data_train[1],data_train[2])
    start_time = time.time()

    scheduler.step()

    model.train()
    avg_loss = 0.
    optimizer.zero_grad()
    count = 0
    for index_batch in tqdm(range(total_batch), disable=False):
        data = data_train[index_batch*batch_size:(index_batch+1)*batch_size]
        x_batch_pic = data[0].cuda()
        x_batch_word = data[1].cuda()
        y_batch = data[-1].cuda()
        y_pred = model(x_batch_pic,x_batch_word)
        loss = loss_fn(y_pred,y_batch)
        loss.backward()
        optimizer.step()
        model.zero_grad()
        avg_loss += loss.item() / len(data_train)
        count = count+1
    elapsed_time = time.time() - start_time
    print('Epoch {}/{} \t loss={:.4f} \t time={:.2f}s'.format(
          epoch + 1, n_epochs, avg_loss, elapsed_time))

    ###################validation data###################
    
    model.eval()
    val_preds = np.zeros((len(valid_word_torch), 1))
    val_loss = 100

    for index_batch in tqdm(range(total_batch_valid), disable=False):
        data = valid_torch_dataset[index_batch*batch_size:(index_batch+1)*batch_size]
        x_batch_pic = data[:-1][0].cuda()
        x_batch_word = data[:-1][1].cuda()
        y_pred = model(x_batch_pic,x_batch_word).detach().cpu().numpy()
        val_preds[index_batch * batch_size:(index_batch+1) * batch_size,:] = y_pred
        
    val_loss = valid_score(valid.reset_index(drop=True),val_preds)
    print('Epoch {}/{} \t val_rmse={:.4f}'.format(
          epoch + 1, n_epochs, val_loss))


    if epoch == 0:
        val_loss_save = val_loss
        torch.save(model, './model/'+model_prefix+'.pkl')
    if early_stopping_mode=='min':
        if val_loss_save>val_loss:
            torch.save(model, './model/'+model_prefix+'.pkl')
            print ('val rmse impoved from {} to {},saving model'.format(
                val_loss_save,val_loss))
            val_loss_save = val_loss

    if early_stopping_mode == 'max':
        if val_loss_save<val_loss:
            torch.save(model, './model/'+model_prefix+'.pkl')
            print ('val rmse impoved from {} to {},saving model'.format(
                val_loss_save,val_loss))
            val_loss_save = val_loss

model = torch.load('./model/'+model_prefix+'.pkl')

###################predict data###################
test_preds = np.zeros((len(test_torch_dataset), 1))
for index_batch in tqdm(range(total_batch_test), disable=False):
    data = test_torch_dataset[index_batch*batch_size:(index_batch+1)*batch_size]
    x_batch_pic = data[0].cuda()
    x_batch_word = data[1].cuda()
    y_pred = model(x_batch_pic,x_batch_word).detach().cpu().numpy()
    test_preds[index_batch * batch_size:(index_batch+1) * batch_size, :] = y_pred
test['pred'+str(fold)]=test_preds


