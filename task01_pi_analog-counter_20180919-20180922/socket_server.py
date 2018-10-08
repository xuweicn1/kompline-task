##sock_server_ssh
# encoding: utf-8
import socket,os
import RPi.GPIO as gpio
import time

ip_port = ("192.168.8.150",50031)
server = socket.socket()  
server.bind(ip_port)
server.listen(5) 

def GetCounter():
	gpio.setmode(gpio.BCM)
	gpio.setup(17,gpio.IN)
	a=0
	while True:
		input_value = gpio.input(17)
		if input_value == False:
			a=a+1
			time.sleep(0.5)
			conn.sendall(str(a))
			while input_value == False:
				input_value = gpio.input(17)
	return 

while True:
	print("接收新指令")
	conn,addr = server.accept()
	print("new conn:",addr)
	print("回传路过人数")
	GetCounter()

server.close()