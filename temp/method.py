
'''组合特征'''
tmp=data.groupby(item,as_index=False)['is_trade'].agg({item+'_buy':'sum', item+'_cnt':'count'})

tmp=data.groupby(item,as_index=False)['is_trade'].agg({item+'_buy': lambda index: index.count(0)})

'''组合特征'''
for i in range(len(items)):
    for j in range(i+1,len(items)):
        egg=[items[i],items[j]]
        tmp = data.groupby(egg, as_index=False)['user_id'].agg({'_'.join([name,items[i],items[j],'cnt']): 'count'})
        train = pd.merge(train, tmp, on=egg, how='left')
        print(egg)


clf = lgb.LGBMClassifier(
    boosting_type='gbdt', num_leaves=31, reg_alpha=0.0, reg_lambda=1,
    max_depth=-1, n_estimators=3000, objective='binary',
    subsample=0.7, colsample_bytree=0.7, subsample_freq=1,  # colsample_bylevel=0.7,
    learning_rate=0.01, min_child_weight=25,random_state=2018,n_jobs=50
    )
clf.fit(train_x, train_y,eval_set=[(train_x,train_y),(test_x,test_y)],early_stopping_rounds=100)
feature_importances=sorted(zip(train_x.columns,clf.feature_importances_),key=lambda x:x[1])
return clf.best_score_[ 'valid_1']['binary_logloss'],feature_importances
