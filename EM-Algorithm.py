#coding=utf-8
""" EM Algorithm """
 
import numpy as np  # 导入numpy包 #
def CalProDensity(sigma, u, x):
    """
            计算x点的概率密度
    """
    result = np.exp(-(x-u)**2/(2*sigma**2))/(sigma*(np.sqrt(2*np.pi)))
    return result
 
def InitData(sigma, u1, u2):
    """
            用numpy包自带的ramdon生成两个随机的正态分布样本，个数都为100个
    """
    data1 = sigma * np.random.randn(10) + u1
    data2 = sigma * np.random.randn(10) + u2
    data = np.append(data1, data2) #将这两个数组拼接到一起#
    return data
 
def StepOfE(data, sigma, u1, u2):
    """
    E操作
            实例xi由第1个和第2个正态分布生成的概率Z
    """
    z = np.zeros([len(data), 2])
    for i, x in enumerate(data): #每执行一次for循环返回数组元素和其数组下标#
        X1 = CalProDensity(sigma, u1, x)
        X2 = CalProDensity(sigma, u2, x)
        z[i,0] = X1 / (X1 + X2)
        z[i,1] = X2 / (X1 + X2)  
    return z 
 
def StepOfM(data, Z):
    """
            极大似然
    """
    u1,u2 = np.dot(np.array(data),np.array(Z))/np.sum(Z,axis=0)
    return u1, u2 
     
def main():
    """
            默认k = 2，默认由两个正态分布组成
    """
    sigma = 4
    u1 = 10
    u2 = 20
    dataSet = InitData(sigma, u1, u2)
    Z = [[], []]
    while True:  #一直迭代至相邻期望值变化非常小时停止迭代#
        preU1 = u1
        preU2 = u2
        Z = StepOfE(dataSet, sigma, u1, u2)
        u1, u2 = StepOfM(dataSet, Z)
        if abs(preU1 - u1) + abs(preU2 - u2) <= 0.001:
            print '拟合后的两个均值为：'
            print 'u1=',u1,'u2=',u2
            break
         
if __name__ == '__main__':
    main()

