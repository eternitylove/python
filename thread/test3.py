#!/usr/bin/env python

import threading
import time

class producer(threading.Thread):
	def run(self):
		global count
		global day
		while True:
			if con.acquire():
				if count>1000:
					con.wait()
				else:
					count=count+100
					msg=self.name+' produce 100,count='+str(count)
					print msg
					con.notify()
				con.release()
				time.sleep(1)
				day -= 1
			if day<0:
				print "produce over"
			exit()

class consumer(threading.Thread):
	def run(self):
		global count
		global day
		while True:
			if con.acquire():
				if count<100:
					con.wait()
				else:
					count=count-3
					msg=self.name+' consumer 3,count='+str(count)
					print msg
					con.notify()
				con.release()
				time.sleep(1)

count=500
day=3
con = threading.Condition()

def test():
	for i in range(1):
		p = producer()
		p.start()
	for i in range(5):
		c=consumer()
		c.start()
test()
