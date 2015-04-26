#!/usr/bin/python

import socket



if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('localhost',8001))
	sock.listen(5)
	while True:
		connection,address = sock.accept()
		print 'connect by',address

		while True:
			buf = connection.recv(1024)

			if not buf:
				break
			connection.send("echo=>"+buf)
		connection.close()

