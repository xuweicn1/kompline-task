# encoding: utf-8
from driverhx711 import HX711
import socket,os
import time

ip_port = ("192.168.0.150",50050)
server = socket.socket()  
server.bind(ip_port)
server.listen(5) 

def sent_counter():
    while True:
        n = HX711(4,17).getdv()
        conn.sendall(str(n))
        time.sleep(5)

while True:
    print("waiting collect...")
    conn,addr = server.accept()
    print("new conn:",addr)
    sent_counter()

server.close()

