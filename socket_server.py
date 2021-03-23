#-*- coding: utf-8 -*-
import socket
import sys
import urllib as ulb
import base64
from _thread import *

url = ''
port = 22333
# message = "GET / HTTP/1.1\r\n\r\n"
ACC_NUM = 10

#Initialize socket
def cre_socket():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Connect established error: %s' %e)
    return s

#Get Remote URL IP 
def get_host_ip(url, port, s):
    try:
        remote_ip = socket.gethostbyname(url)
        if remote_ip == None:
            raise RuntimeError
        print("get addr as {}, url is {}".format(remote_ip, url))
        s.connect((remote_ip, port))
        return remote_ip
    except RuntimeError as e:
        print("cannot get the ip by dns, check your network")
    
#Data Send From Host
def data_send(message, s):
    try:
        data = "REC  " + message + ' \r\n'
        data = data.encode()
        s.sendall(data)
    except socket.error as e:
        print("data send error: %s" %e)
    print("Data send successful")
    # return s 

#Data Receive From Remote
def data_recv(net_es):
    while True:
        try:
            reply = conn_info.recv(4096)  #receive 4k data
            if reply == None:
                break
            reply = reply.decode().rstrip(' \r\n')
            data_send(reply, net_es)
            # print(reply)
        except socket.error as e:
            print(e)
            sys.exit()
    net_es.close()

   
    
#Bind Socket port
def socks_bind(s, ACC_NUM):
    try:
        s.bind((url, port))
        s.listen()
        print("Socket Bind Connected!!!")
    except socket.error as e:
        print("Socket Bind Error At %s:%s " %(url, port))
        sys.exit()

    # return s

if __name__ == '__main__':
    server = cre_socket()
    # ip_addr_url = get_host_ip(url, port, client)
    socks_bind(server, ACC_NUM)
    while True: 
        conn_info, addr = server.accept()
        str_conn_info = str(conn_info).rstrip(')>').split(',', 6)[6].lstrip(' ').split(',')[1]
        print("Socket Connect With: {}, Port:{}".format(addr, str_conn_info))
        start_new_thread(data_recv, (conn_info,))

    server.close()



        