>>> import numpy as np
>>> myarray= np.random.randint(0,2,10)输出只含0,1元素的一维数组,长度为10
>>> myarray
array([1, 1, 1, 0, 1, 0, 0, 1, 1, 0])
>>> myarray= np.random.randint(0,2,(3,10))输出只含0,1元素的3行10列数组
>>> myarray
array([[0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
       [0, 0, 0, 1, 0, 1, 0, 1, 1, 0]])
>>> myarray=np.random.randint(0,2)当第三个参数值省略时,输出只有一个值,随机为0,1
>>> myarray
0
>>> myarray=np.random.randint(0,2)
>>> myarray
0
>>> myarray=np.random.randint(0,2)
>>> myarray
0
>>> myarray=np.random.randint(0,2)
>>> myarray
1
