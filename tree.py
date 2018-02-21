import os
import sys
from hashlib import md5
def roots(path = os.popen('cd; pwd').read().split('\n')[0], space = '', start = 0, end = 1):
	if path == '/':
		if os.popen('whoami').read().split('\n')[0] == 'root':
			files = ' /'
		else:
			print('for run the function roots from root, run this scritp as a superuser')
			exit()
	else:
		files = path.split('/')[len(path.split('/')) - 1]
	os.chdir(path)
	dir = []
	path = []
	pathing2 = os.popen('pwd').read().split('\n')[0]
	ls = os.popen('ls').read().split('\n')
	for i in range(len(ls)):
		if os.path.isdir(ls[i]) == True:
			dir.append(ls[i])
		elif os.path.isfile('./' + ls[i]) == True:
			path.append(ls[i])
	if start + 1 != end:
		print(space[:-1] + '├─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")
	else:
		space = space[:-2] + '  '
		print(space[:-1] + '└─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")
	for i in range(len(path)):
		if i == (len(path) - 1) and len(dir) == 0:
			if start + 1 == end:
				space = space[:-2] + '  '
				print(space + '  └─' + "\033[0;32m" + path[i] + "\033[0;0m")
			else:
				print(space + '  └─' + "\033[0;32m" + path[i] + "\033[0;0m")
		else:
			if start + 1 == end:
				space = space[:-2] + '  '
				print(space + '  ├─' + "\033[0;32m" + path[i] + "\033[0;0m")
			else:
				print(space + '  ├─' + "\033[0;32m" + path[i] + "\033[0;0m")
	for i in range(len(dir)):
		os.chdir(os.popen('cd "' + dir[i] + '"; ' + 'pwd').read().split('\n')[0])
		roots(os.popen('pwd').read().split('\n')[0], space + '  │', i, len(dir))
		os.chdir(pathing2)


def clean(clear = os.popen('cd; pwd').read().split('\n')[0], path = [], delete = [], pwd = [], pwd2 = [], file = []):
	os.chdir(clear)
	pathing2 = clear
	ls = os.popen('ls').read().split('\n')
	if len(ls) - 1 == 0:
		print(os.popen('pwd').read().split('\n')[0] + "\033[1;31m" + ' is empty' + "\033[0;0m")
	else:
		for i in range(len(ls)):
			if os.path.isfile('./' + ls[i]) == True:
				if len(path) != 0:
					for x in range(len(path)):
						if md5(open(ls[i], 'rb').read()).hexdigest() == path[x]:
							pwd2.append(file[x])
							pwd.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
							delete.append(md5(open(ls[i], 'rb').read()).hexdigest())
					if len(delete) != 0:
						if md5(open(ls[i], 'rb').read()).hexdigest() != delete[len(delete) - 1]:
							path.append(md5(open(ls[i], 'rb').read()).hexdigest())
							file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
					elif len(delete) == 0:
						path.append(md5(open(ls[i], 'rb').read()).hexdigest())
						file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
				else:
					path.append(md5(open(ls[i], 'rb').read()).hexdigest())
					file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
			elif os.path.isdir(ls[i]) == True:
				os.chdir(os.popen('cd "' + ls[i] + '"; ' + 'pwd').read().split('\n')[0])
				clean(os.popen('pwd').read().split('\n')[0], path, delete, pwd, pwd2, file)
				os.chdir(pathing2)
		less = 1
		for i in range(len(pwd)):
			print(pwd[i - less] + "\033[1;31m" + ' is same to ' + "\033[0;0m" + pwd2[i - less])
			pwd.remove(pwd[i - less])
			pwd2.remove(pwd2[i - less])
			less = less + 1
