import os
import sys
from hashlib import md5
class Tree:
	clean = {'empty' : {'name' : [], 'path' : []}, 'duplicate' : {'original' : {'path' : [], 'name' : []}, 'name' : [], 'path' : []}}
	roots = {'dir' : {'name' : [], 'path' : []}, 'file' : {'name' : [], 'path' : []}}
	# Roots().roots() var
	start = 0
	end = 1
	space = ''
	# Clean().clean() and Clean.element() array
	dirs = []
	files = []
	clear = []
	delete = []
	pwd = []
	file = []
	# Roots().element() var and array
	x = 0
	# Roots().type()
	type = []

	def __init__(self, path = os.popen('cd; pwd').read().split('\n')[0]):
		self.path = path

class Roots(Tree):
	def __init__(self, path):
		super().__init__(path)
		self.path = path
	# show all element in the path, files and folders
	def element(self):
		Tree.x = Tree.x + 1
		os.chdir(self.path)
		pathing = os.popen('pwd').read().split('\n')[0]
		ls = os.popen('ls').read().split('\n')
		for i in range(len(ls)):
			if os.path.isdir(ls[i]) == True:
				Tree.roots['dir']['path'].append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
				Tree.roots['dir']['name'].append(ls[i])
				os.chdir(os.popen('cd "' + ls[i] + '"; pwd').read().split('\n')[0])
				Roots(os.popen('pwd').read().replace('\n', '')).element()
				os.chdir(pathing)
			elif os.path.isfile('./' + ls[i]) == True:
				Tree.roots['file']['path'].append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
				Tree.roots['file']['name'].append(ls[i])
		Tree.x = Tree.x - 1
		try:
			return Tree.roots
		finally:
			if Tree.x == 0:
				# clear Roots().element() array
				Tree.roots = {}
	# graphic function, show the tree of the path
	def type(self, type):
		Tree.x = Tree.x + 1
		type = type.replace('.', '')
		os.chdir(self.path)
		pathing = os.popen('pwd').read().split('\n')[0]
		ls = os.popen('ls').read().split('\n')
		for i in range(len(ls)):
			if os.path.isdir(ls[i]) == True:
				os.chdir(os.popen('cd "' + ls[i] + '"; pwd').read().split('\n')[0])
				Roots(os.popen('pwd').read().replace('\n', '')).type(type)
				os.chdir(pathing)
			elif os.path.isfile('./' + ls[i]) == True:
				if ls[i].split('.')[len(ls[i].split('.')) - 1] == type:
					Tree.type.append(ls[i])
		Tree.x = Tree.x - 1
		try:
			return Tree.type
		finally:
			if Tree.x == 0:
				Tree.type = []
	# graphic function, show the tree of the path
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
			Roots(os.popen('pwd').read().split('\n')[0]).roots()
			Tree.space = Tree.space[:-3]
			os.chdir(pathing2)
class Clean(Tree):

	def __init__(self, path):
		super().__init__(path)
		self.path = path
	# show empty folders and equal files
	def element(self):
		os.chdir(self.path)
		pathing = os.popen('pwd').read().split('\n')[0]
		ls = os.popen('ls').read().split('\n')
		if len(ls) - 1 == 0:
			Tree.clean['empty']['path'].append(os.popen('pwd').read().split('\n')[0])
			Tree.clean['empty']['name'].append(os.popen('pwd').read().split('\n')[0].split('/')[-1])
		else:
			for i in range(len(ls)):
				if os.path.isdir(ls[i]) == True:
					Tree.dirs.append(ls[i])
					Tree.x = Tree.x + 1
					os.chdir(os.popen('cd "' + ls[i] + '"; pwd').read().split('\n')[0])
					Clean(os.popen('pwd').read().replace('\n', '')).element()
					Tree.x = Tree.x - 1
					os.chdir(pathing)
				elif os.path.isfile('./' + ls[i]) == True:
					if len(Tree.clear) != 0:
						for x in range(len(Tree.clear)):
							if md5(open(ls[i], 'rb').read()).hexdigest() == Tree.clear[x]:
								Tree.clean['duplicate']['path'].append(Tree.files[x])
								Tree.clean['duplicate']['name'].append(Tree.files[x].split('/')[-1])
								Tree.clean['duplicate']['original']['path'].append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])
								Tree.clean['duplicate']['original']['name'].append(ls[i])
								Tree.delete.append(md5(open(ls[i], 'rb').read()).hexdigest())                   # delete
						if len(Tree.delete) != 0:
							if md5(open(ls[i], 'rb').read()).hexdigest() != Tree.delete[len(Tree.delete) - 1]:
								Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                    # clear
								Tree.files.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])       # files
						elif len(Tree.delete) == 0:
							Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                        # clear
							Tree.files.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])           # files
					else:
						Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                            # clear
						Tree.files.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i])               # files
			less = 1
			try:
				return Tree.clean
			finally:
				if Tree.x == 0:
					# clear Clean().element() array
					Tree.dirs = [] #dirs
					Tree.files = [] #files
					Tree.delete = [] #delete
					Tree.clear = [] #clear
					Tree.clean = {}
	# delete empty folders and equal files
	def delete(self, delete = 'both'):
		if delete != 'dirs' and delete != 'files' and delete != 'both':
			print('Arguments not found: the value of this arguments is "dirs" or "files" or "both"')
			exit()
		os.chdir(self.path)
		pathing = os.popen('pwd').read().split('\n')[0]
		ls = os.popen('ls').read().split('\n')
		if len(ls) - 1 == 0:
			Tree.empty.append(os.popen('pwd').read().split('\n')[0])
		else:
			for i in range(len(ls)):
				if os.path.isdir(ls[i]) == True:
					Tree.dirs.append(ls[i])                                                                     # dirs
					os.chdir(os.popen('cd "' + ls[i] + '"; pwd').read().split('\n')[0])
					Tree.x = Tree.x + 1
					Clean(os.popen('pwd').read().replace('\n', '')).delete(delete)
					Tree.x = Tree.x - 1
					os.chdir(pathing)
				elif os.path.isfile('./' + ls[i]) == True:
					if len(Tree.clear) != 0:
						for x in range(len(Tree.clear)):
							if md5(open(ls[i], 'rb').read()).hexdigest() == Tree.clear[x]:                      # pwd2
								Tree.pwd.append(os.popen('pwd').read().replace('\n', '') + '/' + ls[i]) 
								Tree.delete.append(md5(open(ls[i], 'rb').read()).hexdigest())                   # delete
						if len(Tree.delete) != 0:
							if md5(open(ls[i], 'rb').read()).hexdigest() != Tree.delete[len(Tree.delete) - 1]:
								Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                    # clear
						elif len(Tree.delete) == 0:
							Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                        # clear
					else:
						Tree.clear.append(md5(open(ls[i], 'rb').read()).hexdigest())                            # clear
			if Tree.x == 0:
				for i in range(len(Tree.empty)):
					if delete == 'both' or delete == 'dirs':
						os.system('rm -rf "' + Tree.empty[i] + '"')
				for i in range(len(Tree.pwd)):
					if delete == 'both' or delete == 'files':
						os.system('rm -rf "' + Tree.pwd[i] + '"')
				Tree.empty = []
				Tree.pwd = []
				Tree.dirs = []
				Tree.delete = []
				Tree.clear = []
