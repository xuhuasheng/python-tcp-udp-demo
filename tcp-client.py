'''
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2021-11-23 15:55:32
LastEditTime : 2022-01-10 17:55:11
LastEditors  : Xu Huasheng
Copyright (c) 2021 AIRCAS. All rights reserved.
'''
from socket import *
# 创建套接字socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 目的信息
server_ip = "127.0.0.1"
server_port = 8080

# 连接服务器
# tcp客户端一般不绑定，因为是主动链接服务器，所以只要确定好服务器的ip、port等信息就好，本地客户端可以随机
tcp_client_socket.connect((server_ip, server_port))

# while True:
#     send_data = bytes.fromhex("48 49")
#     tcp_client_socket.send(send_data)

recvData = tcp_client_socket.recv(1024)
r = recvData.hex()
print(f"接收到的数据为：{recvData.hex()}")

# 关闭套接字
tcp_client_socket.close()