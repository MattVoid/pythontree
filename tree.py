import os
import sys
from sys import platform
def roots(path = os.popen('pwd').read().split('/')[len(os.popen('pwd').read().split('/')) - 1], space = '', start = 0, end = 1):
	spc = space
	dir = path
	dir = []
	files = path
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
		roots(dir[i], spc + '  │', i, len(dir))
		os.chdir(pathing2)
