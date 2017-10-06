# coding=utf8
#Interpreter:Anaconda include sklearn#
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets.samples_generator import make_blobs
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier

'''随机生成训练的数据集,包含6个特征，2个类标签'''
data, target = make_blobs(n_samples=100, centers=2, n_features=5, cluster_std=[1.0, 3.0])
# print data # for test
# print target # for test
"""
n_samples是待生成的样本的总数。
n_features是每个样本的特征数。
centers表示类别数。
cluster_std表示每个类别的方差，例如我们希望生成2类数据，其中一类比另一类具有更大的方差，可以将cluster_std设置为[1.0,3.0]。
"""

'''模型融合中使用到的各个单模型'''
clfs = [LogisticRegression(),
        RandomForestClassifier(n_estimators=5, n_jobs=-1, criterion='entropy'),
        KNeighborsClassifier(n_neighbors=5),
        ExtraTreesClassifier(n_estimators=5, n_jobs=-1, criterion='entropy'),
        GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, max_depth=6, n_estimators=5)]
"""
n_estimators:生成随机森林的树的数量
n_jobs：为适应和预测而并行运行的作业数。如果-1, 则将作业数设置为内核数
criterion：用于度量拆分的质量的函数。支持的标准是 "基尼" 为基尼杂质和 "熵" 为信息获取。注意: 此参数是特定于树的。

learning_rate：学习率通过 learning_rate 来缩小每棵树的贡献。learning_rate 和 n_estimators 之间有一种权衡。
subsample：用于拟合单个基础学习者的样本的分数
max_depth：个体回归估计的最大深度。最大深度限制树中的节点数。调整此参数以得到最佳性能;最佳值取决于输入变量的交互。
"""

'''切分一半数据作为测试集,另一半为训练集'''
X, X_predict, y, y_predict = train_test_split(data, target, test_size=0.5, random_state=2017)
"""
X:训练集    X_predict:测试集
test_size:表示要包含在测试拆分中的数据集的比例
random_state:用于随机抽样的伪随机数发生器状态
"""
dataset_blend_train = np.zeros((X.shape[0], len(clfs)))
dataset_blend_test = np.zeros((X_predict.shape[0], len(clfs)))

'''5折stacking'''
n_folds = 5
"""
初始化交叉验证对象，y指明有多少个样本；
n_folds指代kfolds中的参数k,表示把训练集分成k份（n_folds份）
"""
skf = list(StratifiedKFold(y, n_folds))

# enumerate函数：遍历数组 #
for j, clf in enumerate(clfs):
    '''依次训练各个单模型'''
    # print(j, clf)
    dataset_blend_test_j = np.zeros((X_predict.shape[0], len(skf)))
    for i, (train, test) in enumerate(skf):
        '''使用第i个部分作为预测，剩余的部分来训练模型，获得其预测的输出作为第i部分的新特征。'''
        X_train = X[train]
        y_train = y[train]
        X_test = X[test]
        y_test = y[test]
        clf.fit(X_train, y_train)
        dataset_blend_train[test, j] = clf.predict(X_test)
        dataset_blend_test_j[:, i] = clf.predict(X_predict)
    '''对于测试集，直接用这k个模型的预测值均值作为新的特征。'''
    dataset_blend_test[:, j] = dataset_blend_test_j.mean(1)

#逻辑回归模型#
clf = LogisticRegression()
#梯度促进分类#
# clf = GradientBoostingClassifier(learning_rate=0.02, subsample=0.5, max_depth=6, n_estimators=30)
clf.fit(dataset_blend_train, y) # 二次训练后的模型 #
result = clf.predict(dataset_blend_test)
print 'dataSet:', dataset_blend_train
print 'The result:', result
