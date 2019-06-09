from glob import glob
import os
from .Element import Element

class Tree:
	clean = {
		"dir": [],
		"duplicate": [],
		"original": []
	}

	roots = {
		"dir": [],
		"file": []
	}

	type = []
	# Roots().roots() var
	start = 0
	end = 1
	space = ''
	#
	md5 = []
	# Roots().element() var and array
	x = 0
	# Roots().type()
	__home = os.getenv("HOME")

	def __init__(self, path = __home):
		self.path = path

class Roots(Tree):
	# show all element in the path, files and folders
	def element(self):
		Tree.x += 1
		os.chdir(self.path) # go to path
		ls = glob("*") # get all file or directory
		for i in ls:
			element = Element(f"{os.getcwd()}/{i}")
			if element.is_dir:
				Tree.roots["dir"].append(element)
				os.chdir(element.path)
				Roots(element.path).element()
				os.chdir("../")
			elif element.is_file:
				Tree.roots["file"].append(element)
		Tree.x -= 1
		try:
			return Tree.roots
		finally:
			if not Tree.x:
				Tree.roots = {'dir': [], 'file': []}

	# graphic function, show the tree of the path
	def type(self, type):
		Tree.x += 1

		if type[0] != ".": type = f".{type}"
		os.chdir(self.path)
		ls = glob("*")
		for i in ls:
			element = Element(f"{os.getcwd()}/{i}")
			if element.is_dir:

				os.chdir(element.path)
				Roots(element.path).type(type)
				os.chdir("../")

			elif element.type == type:
					Tree.type.append(element)
		Tree.x -= 1
		try:
			return Tree.type
		finally:
			if Tree.x == 0: type = []
	# graphic function, show the tree of the path
	def roots(self):

		if self.path == "/" and os.environ["USER"] == 'root':
			files = "/"
		elif self.path == "/" and os.environ["USER"] != 'root':
			print('for run the function roots from root, run this scritp as a superuser')
			exit()
		else:
			files = os.getcwd().split('/')[-1]

		os.chdir(self.path)
		self.path = []
		dir = []
		ls = glob("*")
		for i in ls:
			if os.path.isdir(i): dir.append(i)
			else: self.path.append(i)

		if Tree.start + 1 != Tree.end:
			print(Tree.space[:-1] + '├─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")
		else:
			Tree.space = Tree.space[:-2] + '  '
			print(Tree.space[:-1] + '└─' + "\033[;1m" + files.replace('\n', '') + "\033[0;0m")

		for i in range(len(self.path)):
			if i == len(self.path) - 1 and not len(dir):
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

		for i, element in enumerate(dir):
			os.chdir(f"./{element}")
			Tree.space += '  │'
			Tree.start = i
			Tree.end = len(dir)
			Roots(os.getcwd()).roots()
			Tree.space = Tree.space[:-3]
			os.chdir("../")

class Clean(Tree):
	# show empty folders and equal files
	def element(self):
		Tree.x += 1
		os.chdir(self.path)
		ls = glob("*")
		for i in ls:
			element = Element(f"{os.getcwd()}/{i}")
			if element.is_dir:
				if element.is_empty(): Tree.clean["dir"].append(element)
				os.chdir(element.path)
				Clean(element.path).element()
				os.chdir("../")

			elif element.is_file:
				if element.md5() not in Tree.md5:
					Tree.clean["original"].append(element)
					Tree.md5.append(element.md5())
				else:
					Tree.clean["duplicate"].append(element)
		Tree.x -= 1
		try:
			return Tree.clean
		finally:
			if not Tree.x:
				# clear Clean().element() array
				md5 = []
				clean = {"dir": [], "duplicate": [], "original": []}
	# delete empty folders and equal files
	def delete(self, delete = 'both'):
		if delete != 'dirs' and delete != 'files' and delete != 'both':
			print('Arguments not found: the value of this arguments is "dirs" or "files" or "both"')
		list = self.element()
		if delete == "both" or delete == "dirs":
			for dir in list["dir"]:
				dir.delete()
		if delete == "both" or delete == "files":
			for file in list["duplicate"]:
				file.delete()
