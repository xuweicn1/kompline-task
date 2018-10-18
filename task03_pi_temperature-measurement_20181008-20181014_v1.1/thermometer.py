import numpy as np
import pandas as pd
from scipy import optimize

#利用电阻温度变化关系，生成函数；读取电阻值，返回温度（℃）

class Thermometer:
   
    def f_3(self,x, A, B, C, D):
        return A*x*x*x + B*x*x + C*x + D
     
    def read(self,x):
        data = pd.read_csv("data/data2_0-200.csv")     #Read data
        astype_data = data.values.astype(np.float32)     #Transform into an array
        x0= np.reshape(astype_data[:,1],len(astype_data[:,1]))    #电阻值 x0
        y0 = np.reshape(astype_data[:,0],len(astype_data[:,0]))     #温度 y0
        A, B, C, D= optimize.curve_fit(self.f_3, x0, y0)[0]
        T = A*x*x*x + B*x*x + C*x + D
        return T
