import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
 
#三次曲线方程
def f_3(x, A, B, C, D):
    return A*x*x*x + B*x*x + C*x + D

def plot_test():
 
    plt.figure()

    #拟合点
    data = pd.read_csv("r-count_1017.csv")   #Read data
    train_data = data.values.astype(np.float32)     #Transform into an array
    x_ = train_data[:,1]    #读取的是列 需要转置
    x0= np.reshape(x_,len(x_))	#x0
    y_ = train_data[:,0]
    y0 = np.reshape(y_,len(y_))		# y0
 
    #绘制散点
    plt.scatter(x0[:], y0[:], 5, "red") #5像素 红色

    #三次曲线拟合与绘制
    A3, B3, C3, D3= optimize.curve_fit(f_3, x0, y0)[0]
    x3 = np.arange(0, 400, 0.01)
    y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3 
    print("三次曲线参数：",A3, B3, C3, D3) #系数
    plt.plot(x3, y3, "purple")  #展示函数 紫色

    plt.title("test")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
 
    return

plot_test()
