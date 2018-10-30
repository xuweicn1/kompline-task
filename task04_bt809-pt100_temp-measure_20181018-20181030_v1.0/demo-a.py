#!/usr/bin/env python
import time
import serial
from bt809 import BT809

bt = BT809()
with serial.Serial('com4',4800,timeout=1) as ser:
    while 1:
        s = '8181521B'
        ser.write(bytes.fromhex(s))
        r = ser.readline().hex()
        ct = bt.r_ct(r)
        print('当前温度值是：',ct,'℃')
        print("***********************")
        time.sleep(1)