#!/usr/bin/env python3
import socket

s=socket.socket()
host='192.168.56.1'
port=int(input("Enter the PORT:"))

s.connect((host,port))
while True:
	data =str(s.recv(1024)).strip('b').strip('\'')
	print(data)
	msg=bytes("reciever >>> "+input(r""),encoding='utf-8')
	s.send(msg)
