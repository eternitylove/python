#!/usr/bin/python
import sys
import socket
import time

if __name__ == '__main__':
	serverhost = 'localhost'
	serverport = 8001
	message = ["hello world"]
	if len(sys.argv)>1:
		serverhost=sys.argv[1]
		if len(sys.argv)>2:
			message = sys.argv[2]
		
			print message
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((serverhost,serverport))
	for line in message:
		sock.send(line)
		print sock.recv(1024)
	sock.close()
