#!/usr/bin/env python

import os
import time

DESK = "/home/server/test/"

SAVE_FILE = "/home/server/helle"

FILE_EXT = ['bmp','jpeg','gif']

my_dirs = []
my_files = []

FILES_NUMBER = 0
RIGHT_FILES_NUMBER = 0
NOT_RIGHT_FILES_NUMBER = 0

DIR_NUMBER = 0

def listdir(dir_path):
	if os.path.exists(dir_path):
		return os.listdir(dir_path)
	else:
		return "dir:"+dir_path+" not exist"

def search_files(path,name):
	if not os.path.isdir(path) and not os.path.isfile(path):
		return False
	path = os.path.join(path,name)
#	print(path)
	if os.path.isfile(path):
		global FILES_NUMBER
		FILES_NUMBER = FILES_NUMBER+1
		lists = path.split('.')
		file_ext = lists[-1]
		if file_ext in FILE_EXT:
			global RIGHT_FILES_NUMBER
	        	RIGHT_FILES_NUMBER +=1
		    	global my_files 
			now = str(time.strftime('%Y-%m-%d %H:%M:%s',time.localtime(time.time())))
			size = str(get_file_size(path))

			my_files.append(now+' '+path+' '+size+'\n')
			print('file:',path)
		else :
			global NOT_RIGHT_FILES_NUMBER
			NOT_RIGHT_FILES_NUMBER +=1

	elif os.path.isdir(path):
		global DIR_NUMBER
		DIR_NUMBER +=1
		for name in listdir(path):
			search_files(path,name)
def get_file_size(path):
	if os.path.exists(path):
		return os.path.getsize(path)

def write_info(content):
	if os.path.exists(path):
		with open(SAVE_FILE,"w+") as fp:
			fp.write(content)
			fp.flush()
			fp.close()
	else:
		print('file :not exit'.format(SAVE_FILE))
def read_info():
	if os.path.exists(path):
		fp=open(SAVE_FILE,"r+")
		for line in fp:
			print(line)
	else :
	 	print("file:{} not exit\n".format(SAVE_FILE))

if __name__ == '__main__':
	for d in listdir(DESK):
		my_dirs.append(os.path.join(DESK,d))
#	print(my_dirs)
	my_dir = ['/home/server/']
	for path in my_dir:
	 	search_files(path,'')
	print("#"*50)
#	print(my_files)
	print('#'*50)
	print('start write info')
	content = ''.join(my_files)
	write_info(content)
	print('#'*50)
	print('start read info')
	read_info()
	print('#'*50)

