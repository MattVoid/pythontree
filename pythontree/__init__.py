import os
import sys
from hashlib import md5
class Tree:
	start = 0
	end = 1
	space = ''
	clear = []
	delete = []
	pwd = []
	pwd2 = []
	file = []

	def __init__(self, path = os.popen('cd; pwd').read().split('\n')[0]):
		self.path = path

	def roots(self):
		if self.path == '/':
			if os.popen('whoami').read().split('\n')[0] == 'root':
				files = ' /'
			else:
				print('for run the function roots from root, run this scritp as a superuser')
				exit()
		else:
			files = self.path.split('/')[len(self.path.split('/')) - 1]
		os.chdir(self.path)
		self.path = []
		dir = []
		pathing2 = os.popen('pwd').read().split('\n')[0]
		ls = os.popen('ls').read().split('\n')
		for i in range(len(ls)):
			if os.path.isdir(ls[i]) == True:
				dir.append(ls[i])
			elif os.path.isfile('./' + ls[i]) == True:
				self.path.append(ls[i])
		if Tree.start + 1 != Tree.end:
			print(Tree.space[:-1] + '├─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")
		else:
			Tree.space = Tree.space[:-2] + '  '
			print(Tree.space[:-1] + '└─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")
		for i in range(len(self.path)):
			if i == (len(self.path) - 1) and len(dir) == 0:
				if Tree.start + 1 == Tree.end:
					Tree.space = Tree.space[:-2] + '  '
					print(Tree.space + '  └─' + "\033[0;32m" + self.path[i] + "\033[0;0m")
				else:
					print(Tree.space + '  └─' + "\033[0;32m" + self.path[i] + "\033[0;0m")
			else:
				if Tree.start + 1 == Tree.end:
					Tree.space = Tree.space[:-2] + '  '
					print(Tree.space + '  ├─' + "\033[0;32m" + self.path[i] + "\033[0;0m")
				else:
					print(Tree.space + '  ├─' + "\033[0;32m" + self.path[i] + "\033[0;0m")
		for x in range(len(dir)):
			os.chdir(os.popen('cd "' + dir[x] + '"; pwd').read().split('\n')[0])
			Tree.space = Tree.space + '  │'
			Tree.start = x
			Tree.end = len(dir)
			Tree(os.popen('pwd').read().split('\n')[0]).roots()
			Tree.space = Tree.space[:-3]
			os.chdir(pathing2)
	def clean(self):
		os.chdir(self.path)
		pathing2 = self.path
		ls = os.popen('ls').read().split('\n')
		if len(ls) - 1 == 0:
			print(os.popen('pwd').read().split('\n')[0] + "\033[1;31m" + ' is empty' + "\033[0;0m")
		else:
			for i in range(len(ls)):
				if os.path.isfile('./' + ls[i]) == True:
					if len(Tree.clear) != 0:
						for x in range(len(Tree.clear)):
							if md5(open(ls[i], 'rb').read()).hexdigest() == Tree.clear[x]:
								Tree.pwd2.append(Tree.file[x])
								Tree.pwd.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
								Tree.delete.append(md5(open(ls[i], 'rb').read()).hexdigest())
						if len(Tree.delete) != 0:
							if md5(open(ls[i], 'rb').read()).hexdigest() != Tree.delete[len(Tree.delete) - 1]:
								Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())
								Tree.file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
						elif len(Tree.delete) == 0:
							Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())
							Tree.file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
					else:
						Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())
						Tree.file.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
				elif os.path.isdir(ls[i]) == True:
					os.chdir(os.popen('cd "' + ls[i] + '"; ' + 'pwd').read().split('\n')[0])
					Tree(os.popen('pwd').read().split('\n')[0]).clean()
					os.chdir(pathing2)
			less = 1
			for i in range(len(Tree.pwd)):
				print(Tree.pwd[i - less] + "\033[1;31m" + ' is same to ' + "\033[0;0m" + Tree.pwd2[i - less])
				Tree.pwd.remove(Tree.pwd[i - less])
				Tree.pwd2.remove(Tree.pwd2[i - less])
				less = less + 1