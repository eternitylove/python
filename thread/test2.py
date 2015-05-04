#!/usr/bin/env python

import threading
import time

class mythread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(1)
			print 'i am '+self.name + str(i)

def test():
	for i in range(2):
		t=mythread()
		t.start()
test()
