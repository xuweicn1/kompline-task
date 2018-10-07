##socket_server_client
# encoding: utf-8
import socket

ip_port = ("192.168.8.150",50031)
client = socket.socket()
client.connect(ip_port)

while True:
	data=client.recv(1024)
	print("\n路过人数:",int(data))
client.close()