#!/usr/bin/env python
import time
import serial
from bt809 import BT809

bt = BT809()

with serial.Serial('com4',4800,timeout=1) as ser:
    for comd in bt.r_csv("input/preset-temp_(1-10).csv"):
        ser.write(bytes.fromhex(comd))
        r = ser.readline().hex()
        st = bt.r_st(r)
        bt.w_txt(str(st))
        # print('设定温度值是：',st,'℃')
        print("***********************")
        time.sleep(1)