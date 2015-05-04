#!/usr/bin/env python

import threading
import time
from Queue import *

class producer(threading.Thread):
	def run(self):
		global queue
		count=0
		while True:
			for i in range(100):
				if queue.qsize()>1000:
					pass
				else:
					count = count+1
					msg = "produce "+str(count)
					queue.put(msg)
					print msg
			time.sleep(1)
	
class consumer(threading.Thread):
	def run(self):
		global queue
		while True:
			for i in range(3):
				if queue.qsize()<100:
					pass
				else:
					msg = "consumer "+queue.get()
					print msg
			time.sleep(1)
queue = Queue()
def test():
	for i in range(500):
		queue.put("chushichanping"+str(i))
	for i in range(2):
		p = producer()
		p.start()
	for i in range(5):
		c = consumer()
		c.start()
test()
