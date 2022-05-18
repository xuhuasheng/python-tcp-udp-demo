'''
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2021-11-23 15:55:07
LastEditTime : 2021-12-22 21:41:17
LastEditors  : Xu Huasheng
Copyright (c) 2021 AIRCAS. All rights reserved.
'''
from socket import *
tcp_serve_socket = socket(AF_INET, SOCK_STREAM) # IPv4 TCP数据流

# 本地信息
server_ip = "192.168.137.1"     # 本地连接的host地址，ipconfig查看
server_port = 8080              # 端口号 自己定
address = (server_ip, server_port)
# tcp服务器一般情况下都需要绑定，否则客户端找不到这个服务器
tcp_serve_socket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
# listen里的数字表征同一时刻能连接客户端的程度.
tcp_serve_socket.listen(128)

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
# clientAddr 是元组（ip，端口）
clinet_socket, clientAddr =  tcp_serve_socket.accept()
print(clientAddr)
recv_data = clinet_socket.recv(1024)    # 接收1024个字节
print(f"接收到的数据为：{recv_data.decode('gbk')}")

clinet_socket.send("thank you!".encode('gbk'))

clinet_socket.close()
tcp_serve_socket.close()