#!/usr/bin/env python
import time
import serial
import pandas as pd
import numpy as np
import csv


class BT809:
    #批量读取csv文件，返回csv文件一行BT809命令
    def r_csv(self,path):
        data = pd.read_csv(path)
        astype_data = data.values.astype(np.str)
        read = np.reshape(astype_data[:,0],len(astype_data[:,0]))
        return read

    #将结果追加hex_df.csv中
    def w_txt(self,x):
        with open("output/set_temp.txt","a") as f:
            f.write(x)
            f.write("\n")

    #读取bt809，返回温度值
    def r_ct(self,x):
        ct0 = '{}{}'.format(x[2:4],x[:2])
        ct  =  int(ct0,16)/10
        return ct

    #读取bt809，返回设定值
    def r_st(self,x):
        st0 = '{}{}'.format(x[6:8],x[4:6])
        st  = int(st0,16)/10
        return st

    #输入读取命令，bt809返回16位字符串
    def bt809_r(self,x):
        by = bytes.fromhex(x)             #转型：str-->bytes
        ser.write(by)                   #向bt809输入读取命令
        r= ser.readline().hex()    #返回一个16进制字节，转型为str
        return r

        




