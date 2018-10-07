import numpy as np
#生成一个元素值位0-10之间的大小为10*10的矩阵
a = np.mat(np.random.randint(10,size=(10,10)))
b = a.I #a的逆矩阵
print('随机一个10*10的矩阵:\n',a)
print('随机矩阵的逆矩阵:\n',b)