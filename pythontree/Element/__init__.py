import os
from hashlib import md5
from glob import glob
import shutil

class Element:
	""" The class to manage the element """
	def __init__(self, path):
		self._path = path
		self._name = path.split('/')[-1]
		self._is_file = os.path.isfile(self._path)
		self._is_dir = os.path.isdir(self._path)
		if self._is_file:
			self._type = os.path.splitext(self._name)[1]
		elif self._is_dir:
			self._type = None

	def __repr__(self):
		return f"Element('{self._path}'"

	def __str__(self):
		return f"{self._name}"

	def __bool__(self):
		return os.path.isfile(self._path) or os.path.isdir(self._path)

	@property
	def name(self):
		return self._name

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):
		self._path = value
		self._name = value.split('/')[-1]
		self._is_file = os.path.isfile(self._path)
		self._is_dir = os.path.isdir(self._path)
		if self._is_file:
			self._type = os.path.splitext(self._name)[1]
		elif self._is_dir:
			self._type = None

	@property
	def type(self):
		return self._type

	@property
	def is_file(self):
		return self._is_file

	@property
	def is_dir(self):
		return self._is_dir

	def delete(self):
		""" This method delete the file or directory"""
		if self._is_file:
			os.remove(self._path)
		elif self._is_dir:
			shutil.rmtree(self._path)

	def is_empty(self):
		""" This method check if element is empty or not """
		if self._is_file:
			if self.md5() == "d41d8cd98f00b204e9800998ecf8427e": return True
			else: return False
		elif self._is_dir:
			ls = glob(f"{self._path}/*")
			if len(ls) == 0: return True
			else: return False

	def md5(self):
		""" This method return md5 of file or None if is directory """
		if self._is_file:
			return md5(open(self._path, 'rb').read()).hexdigest()
		elif self._is_dir:
			return False
