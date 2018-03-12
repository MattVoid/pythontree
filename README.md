# Pythontree

![PyPI - Python Version](https://img.shields.io/badge/Python->=_3.4-blue.svg)
[![Hex.pm](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://github.com/MattVoid/pythontree/blob/master/LICENSE.md)
[![PyPI - Pypi.org Library](https://img.shields.io/badge/pypi-pythontree-brightgreen.svg)](https://pypi.org/search/?q=pythontree)
![Project Version](https://img.shields.io/badge/version-1.5-lightgrey.svg)
	

This project has been created to facilitate folder management

* ### OS Supported ###

	![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
	![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg) 
	![Windows Not_Supported](https://img.shields.io/badge/Windows-Not_Supported-red.svg)

* ### Installation ###
	* pip
		```
		$ pip3 install pythontree
		$ pip3 install pythontree --upgrade
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
		>>> print(Roots.element()['file']['path'])
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
		import pythontree
		Roots = pythontree.Roots('*** you can choose the path from start ***')
		Roots.type('*** insert extension to return ***')
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
		>>> print(Clean.element()['duplicate']['original']['path'])
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
