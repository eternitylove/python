#!/usr/bin/env python

import os,sys,string
import MySQLdb

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='xxxx',db="test")
except Exception,e:
	print e
	sys.exit()

cursor = conn.cursor()
sql = "create table if not exists test1(name varchar(128) primary key,age int(4))"
cursor.execute(sql)
sql = "insert into test1(name,age) values ('%s',%d)"%("zhouwei",23)
try:
	cursor.execute(sql)
except Exception,e:
	print e

sql = "insert into test1(name,age) values ('%s',%d)"%("zhangsan",21)

try:
	cursor.execute(sql)
except Exception,e:
	print e

sql = "insert into test1(name,age) values(%s,%s)"
val = (("lisi",24),("wangwu",24),("hongliu",87))

try:
	cursor.executemany(sql,val)
except Exception,e:
	print e

sql = "select * from test1"
cursor.execute(sql)
alldata = cursor.fetchall()
if alldata:
	for rec in alldata:
		print rec[0],rec[1]

cursor.close()
conn.close()
