import numpy as np
import pandas as pd
from scipy import optimize

#利用电阻电压变化关系，HX711根据压差输出count，读取count生成函数，返回电阻（Ω）

class ResMeasure:
   
    def f_3(self,x, A, B, C, D):
        return A*x*x*x + B*x*x + C*x + D
     
    def get_res(self,x):
        data = pd.read_csv("data/r-c-dv-100.csv")     #Read data
        astype_data = data.values.astype(np.float32)     #Transform into an array
        x0= np.reshape(astype_data[:,1],len(astype_data[:,1]))    #压差取数 x0
        y0 = np.reshape(astype_data[:,0],len(astype_data[:,0]))     #电阻 y0
        A, B, C, D= optimize.curve_fit(self.f_3, x0, y0)[0]
        r = A*x*x*x + B*x*x + C*x + D
        return r
