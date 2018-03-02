# Pythontree

This project has been created to facilitate folder management

* ### Installation ###
	* pip
		```
		$ pip3 install pythontree
		$ pip3 install pythontree --upgrade #upgrade
		```
	* wget
		```
		$ git clone https://github.com/MattVoid/pythontree.git
		$ cd pythontree
		$ python3 setup.py install
		```
* ### Roots ###
	* roots </br>
		it's a grapich function, print a tree of the chosen path
		```
		import pythontree
		Roots = pythontree.Roots('*** you can choose the path to start ***')
		Roots.roots()
		```
		![Alt text](https://raw.githubusercontent.com/MattVoid/pythontree/master/img/roots.jpg?raw=true)
	* element </br>
		return an array with files or folders starting from your chosen path
		```
		import pythontree
		Roots = pythontree.Roots('*** you can choose the path to start ***')
		Roots.element()[0] #return files
		Roots.element()[1] #return folders
		```
* ### Clean ###
  	* element </br>
		return an array with empty folders or equal files
		```
		import pythontree
		Clean = pythontree.Clean('*** you can choose the path to start ***')
		Clean.element()[0] #return empty folders
		Clean.element()[1] #return equal files to the first
		Clean.element()[2] #return first file path
		```
	* delete
		* files </br>
			delete equal files starting from your chosen path
			```
			import pythontree
			Clean = pythontree.Clean('*** you can choose the path to start ***')
			Clean.delete('files')
			```
		* dirs </br>
			delete empty folders starting from your chosen path
			```
			import pythontree
			Clean = pythontree.Clean('*** you can choose the path to start ***')
			Clean.delete('dirs')
			```
		* both </br>
			delete empty folders and equal files starting from your chosen path
			```
			import pythontree
			Clean = pythontree.Clean('*** you can choose the path to start ***')
			Clean.delete('both')
			```
