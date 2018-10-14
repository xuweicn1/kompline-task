# encoding: utf-8
from thermometer import Thermometer
from resmeasure import ResMeasure
import socket

ip_port = ("192.168.0.150",50050)
client = socket.socket()
client.connect(ip_port)

while True:
    cont = client.recv(1024)
    c = float(cont)/100
    r = ResMeasure().get_res(c)
    t = Thermometer().read(r)
    # print('当前电阻是：','%.2f' % r,'Ω')
    print('当前温度是：','%.2f' % t,'℃')
client.close()