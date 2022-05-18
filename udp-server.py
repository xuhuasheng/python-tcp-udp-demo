'''
Description  : 
Version      : 1.0.0
Author       : Xu Huasheng
Date         : 2022-01-13 14:23:43
LastEditTime : 2022-01-13 16:10:14
LastEditors  : Xu Huasheng
Copyright (c) 2022 AIRCAS. All rights reserved.
'''
import socket
BUFSIZE = 1024
IP_PORT = ('127.0.0.1', 7788)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4 udp协议
server.bind(IP_PORT)    # 服务器绑定ip和端口
while True:
    # udp服务器，第一次启动时，一定是先接收数据，在发送数据，一问一答式
    data, client_addr = server.recvfrom(BUFSIZE)
    print('server收到的数据', data)
    server.sendto(b'abcd', client_addr) # 回复客户端

    # 其实服务器也可以直接主动发送，只要知道客户端的ip和port
    # client_addr = ('127.0.0.1', 8080)
    # server.sendto(b'abcd', client_addr) # 回复客户端
    # data, addr = server.recvfrom(BUFSIZE)
    # print(data)
    
server.close()