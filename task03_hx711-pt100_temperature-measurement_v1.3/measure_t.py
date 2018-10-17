# encoding: utf-8
from driverhx711 import HX711
from driverhx711  import Thermometer
from driverhx711  import ResMeasure
import time


while True:
    cont=HX711(4,17).getdv()
    c= float(cont)/100
    r=ResMeasure().get_res(c)
    t = Thermometer().read(r)
    print('当前电阻是：','%.2f' % r,'Ω')
    print('当前温度为：','%.2f' % t,'℃')
    print('*********************')
    time.sleep(5)

