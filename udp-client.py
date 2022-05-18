"""
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2022-01-13 14:24:25
LastEditTime : 2022-05-18 15:42:27
LastEditors  : Xu Huasheng
Copyright (c) 2022 AIRCAS. All rights reserved.
"""
'''
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2022-01-13 14:24:25
LastEditTime : 2022-01-13 15:37:45
LastEditors  : Xu Huasheng
Copyright (c) 2022 AIRCAS. All rights reserved.
'''
import socket 
BUFSIZE = 1024
IP_PORT = ('127.0.0.1', 8080)

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = "hello world"
    client.sendto(msg.encode('utf-8'), IP_PORT)     # 客户端询问服务端
    data, server_addr = client.recvfrom(BUFSIZE)    # 等待服务器回复，阻塞式
    print('客户端recvfrom ', data, server_addr)
 
client.close()