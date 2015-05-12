#!/usr/bin/env python


def isrunyear(year):
	if year<0 :
		print 'please input a int'

	if year%400==0 or (year%4==0 and year%100 != 0):
		print '%d is runnian'%year
	else :
	 	print '%d not runnian'%year

for i in range(1000,1200):
	isrunyear(i)

