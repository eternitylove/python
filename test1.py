#!/usr/bin/env python

import os

def visitdir(path):
	for root,dirs,files in os.walk(path):
		print "================================================="
		print "currentdir is :"
		print root

		print "contained follow dir:"
		for dd in dirs:
			print dd
		print "contained follow files:"
		for ff in files:
			print ff
		
#print os.path.join(root,filespath)
visitdir(".")
