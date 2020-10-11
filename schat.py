#!/usr/bin/env python3
import socket

s=socket.socket()
host='192.168.56.1'
port=int(input("enter the PORT: "))
s.bind((host,port))
s.listen(10)

c,addr=s.accept()
print("Got connection with:",addr)
while True:
	msg=bytes("vishnu >>> "+input(r""),encoding='utf-8')
	c.send(msg)
	data=str(c.recv(1024)).strip('b').strip('\'')
	print(data)

#run>>> """telnet localhost port number u enter."""on another terminal
#for local host 
