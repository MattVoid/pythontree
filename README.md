# Element #
The element class is use to manage easier the file or directory from pythontree class
```
└─home
  └─Desktop
    ├─document
    │ └─setup.py
    ├─python
    │ └─try.py
    └─ruby
      └─try.rb
```
```
>>> import Element
>>> element = Element("home/Desktop/document/setup.py")
```
* attributes
	* path </br>
		in the "path" attribute there is the file or directory path
		```
		>>> element.path
		'home/Desktop/document/setup.py'
		```
	* name </br>
		in the "name" attribute there is the file or directory name
		```
		>>> element.name
		'setup.py'
		```
	* type </br>
		in the "type" attribute there is the file or directory type
		```
		>>> element.type
		'.py'
		```
	* is_file </br>
		in the "is_file" attribute there is a bool True value if is file if not False
		```
		>>> element.is_file
		True
		```
	* is_dir </br>
		in the "is_dir" attribute there is a bool True value True if is dir if not False
		```
		>>> element.is_file
		False
		```
* classes
	* is_empty </br>
		the "is_empty" class return a bool True value if the file or directory is empty if not False
		```
		>>> element.is_empty()
		True
		```
	* md5 </br>
		the "md5" class return the md5 of file and return False if element is directory
		```
		>>> element.md5()
		'd41d8cd98f00b204e9800998ecf8427e'
		```
	* delete </br>
		the "delete" class delete file or directory
		```
		>>> element.delete()
		```
		```
		└─home
		  └─Desktop
		    ├─document
		    ├─python
		    │ └─try.py
		    └─ruby
		      └─try.rb
		```

# Pythontree

[![PyPI - Python Version](https://img.shields.io/badge/Python->=_3.4-blue.svg)](https://www.python.org/)
[![Hex.pm](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://github.com/MattVoid/pythontree/blob/master/LICENSE.md)
[![PyPI - Pypi.org Library](https://img.shields.io/badge/pypi-pythontree-brightgreen.svg)](https://pypi.org/search/?q=pythontree)
![Project Version](https://img.shields.io/badge/version-1.5.5-lightgrey.svg)


This project has been created to facilitate folder management

* ### OS Supported ###

	![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
	![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg)
	![Windows Not_Supported](https://img.shields.io/badge/Windows-Not_Supported-red.svg)

* ### Installation ###
	* pip
		```
		# pip3 install pythontree
		# pip3 install pythontree --upgrade
		```
	* git
		```
		$ git clone https://github.com/MattVoid/pythontree.git
		$ cd pythontree
		$ python3 setup.py install
		```
* ### Roots ###
	* roots </br>
		it's a grapich function, print a tree of the chosen path
		```
		>>> import pythontree
		>>> Roots = pythontree.Roots('*** you can choose the path to start ***')
		>>> Roots.roots()
		```
		![Alt text](https://raw.githubusercontent.com/MattVoid/pythontree/master/img/roots.jpg?raw=true)
	* element </br>
		return an array with files or folders starting from your chosen path
		```
		└─home
		  └─Desktop
		    ├─document
		    │ └─setup.py
		    ├─python
		    │ └─try.py
		    └─ruby
		      └─try.rb
		```
		```
		>>> import pythontree
		>>> Roots = pythontree.Roots('/home') # you can choose the path to start
		>>> print(Roots.element())
		['/home/Desktop/document/setup.py', '/home/Desktop/python/try.py', '/home/Desktop/ruby/try.rb']
		>>> print(Roots.element()['file']['name'])
		['setup.py', 'try.py', 'try.rb']
		>>> print(Roots.element()['dir']['path'])
		['/home/Desktop', '/home/Desktop/document', '/home/Desktop/python', '/home/Desktop/ruby']
		>>> print(Roots.element()['dir']['name'])
		['Desktop', 'document', 'python', 'ruby']
		```
	* type </br>
		return an array with files with an extension of your choice starting from your path
		```
		>>> import pythontree
		>>> Roots = pythontree.Roots('/home') # you can choose the path to start
		>>> print(Roots.type('rb')['name']) # you can choose the extension to return
		['try.rb']
		>>> print(Roots.type('rb')['path'])
		['/home/Desktop/ruby/try.rb']
		```
* ### Clean ###
  	* element </br>
		return an array with empty folders or equal files
		```
		└─home
		  └─Desktop
		    ├─document
		    │ └─setup.py
		    ├─python
		    │ ├─try.py
		    │ ├─try(copy).py
		    │ ├─try(copy 2).py
		    │ └─pythontree.py
		    ├─ruby
		    │ └─try.rb
		    └─project
		```
		```
		>>> import pythontree
		>>> Clean = pythontree.Clean('/home') # you can choose the path to start
		>>> print(Clean.element()['empty']['path'])
		['/home/Desktop/project']
		>>> Clean.element()['empty']['name']
		['project']
		>>> print(Clean.element()['duplicate']['path'])
		['/home/Desktop/python/try(copy).py', '/home/Desktop/python/try(copy 2).py']
		>>> print(Clean.element()['duplicate']['name'])
		['try(copy).py','try(copy 2).py']
		>>> print(Clean.element()['duplicate']['original']['path']) #original returns the reference file
		['/home/Desktop/python/try.py','/home/Desktop/python/try.py']
		>>> print(Clean.element()['duplicate']['original']['name'])
		['try.py','try.py']
		```
	* delete
		* files </br>
			delete equal files starting from your chosen path
			```
			>>> import pythontree
			>>> Clean = pythontree.Clean('*** you can choose the path to start ***')
			>>> Clean.delete('files')
			```
		* dirs </br>
			delete empty folders starting from your chosen path
			```
			>>> import pythontree
			>>> Clean = pythontree.Clean('*** you can choose the path to start ***')
			>>> Clean.delete('dirs')
			```
		* both </br>
			delete empty folders and equal files starting from your chosen path
			```
			>>> import pythontree
			>>> Clean = pythontree.Clean('*** you can choose the path to start ***')
			>>> Clean.delete('both')
			```
