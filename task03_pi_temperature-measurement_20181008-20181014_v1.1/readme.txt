树莓派放入：driverhx711.py  sentdv.py ，用来读取压差数据，并将数据发送给客户端

运行sentdv.py，等待客户端连接

客户端运行main_client.py，连接树莓派后，读取压差数值，并转为温度数值。

相对于最先的版本修改了，否则 3.0之后的版本 报错
" a bytes-like object is required, not 'str' "
client_socket.send(data)
client_socket.send(data.encode())

data = client_socket.recv(512)
data = client_socket.recv(512).decode()