import os
import sys
from sys import platform
from hashlib import md5

def roots(path = os.popen('pwd').read().split('\n')[0], space = '', start = 0, end = 1):
	os.chdir(path)
	spc = space
	dir = path.split('/')[len(os.popen('pwd').read().split('/')) - 1]
	dir = []
	files = path.split('/')[len(os.popen('pwd').read().split('/')) - 1]
	path = []
	pathing2 = os.popen('pwd').read().split('\n')[0]
	ls = os.popen('ls').read().split('\n')
	for i in range(len(ls) - 1):
		if os.path.isdir(ls[i]) == True:
			path.append(ls[i])
			dir.append(ls[i])

		elif os.path.isfile('./' + ls[i]) == True:
			path.append(ls[i])
	if start + 1 != end:
		print(spc[:-1] + '├─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m", end = '\n')
	else:
		spc = spc[:-2] + '  '
		print(spc[:-1] + '└─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m", end = '\n')
	for i in range(len(path)):
		if os.path.isfile(path[i]) == True:
			if i == (len(path) - 1) and len(dir) == 0:
				if start + 1 == end:
					spc = spc[:-2] + '  '
					print(spc + '  └─' + "\033[0;32m" + path[i] + "\033[0;0m", end = '\n')
				else:
					print(spc + '  └─' + "\033[0;32m" + path[i] + "\033[0;0m", end = '\n')
			else:
				if start + 1 == end:
					spc = spc[:-2] + '  '
					print(spc + '  ├─' + "\033[0;32m" + path[i] + "\033[0;0m", end = '\n')
				else:
					print(spc + '  ├─' + "\033[0;32m" + path[i] + "\033[0;0m", end = '\n')

	for i in range(len(dir)):
		os.chdir(os.popen('cd "' + dir[i] + '"; ' + 'pwd').read().split('\n')[0])
		roots(os.popen('pwd').read().split('\n')[0], spc + '  │', i, len(dir))
		os.chdir(pathing2)

def clean(clear = os.popen('pwd').read().split('\n')[0]):
	os.chdir(clear)
	path = []
	delete = []
	pwd = []
	pwd2 = []
	pathing2 = clear
	ls = os.popen('ls').read().split('\n')
	for i in range(len(ls)):
		if os.path.isfile('./' + ls[i]) == True:
			if len(path) != 0:
				for x in range(len(path)):
					if md5(open(ls[i], 'rb').read()).hexdigest() == path[x]:
						pwd2.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[x])
						pwd.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
						delete.append(md5(open(ls[i], 'rb').read()).hexdigest())
				if len(delete) != 0:
					if md5(open(ls[i], 'rb').read()).hexdigest() != delete[len(delete) - 1]:
						path.append(md5(open(ls[i], 'rb').read()).hexdigest())
				elif len(delete) == 0:
					path.append(md5(open(ls[i], 'rb').read()).hexdigest())
			else:
				path.append(md5(open(ls[i], 'rb').read()).hexdigest())
		elif os.path.isdir(ls[i]) == True:
			os.chdir(os.popen('cd "' + ls[i] + '"; ' + 'pwd').read().split('\n')[0])
			clean(os.popen('pwd').read().split('\n')[0])
			os.chdir(pathing2)
	for i in range(len(delete)):
		print("\033[;1m" + pwd[i] + "\033[1;31m" + ' is same to ' + "\033[;1m" + pwd2[i] + "\033[0;0m")
		print("\033[0;32m" + delete[i] + "\033[0;0m")
