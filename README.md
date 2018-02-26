# Pythontree

This project has been created to facilitate folder management

* ### Installation ###
	* pip
		```
		$ pip3 install pythontree
		$ pip3 install pythontree --upgrade #upgrade
		```
	*wget
		```
		$ git clone https://github.com/MattVoid/pythontree.git
		$ cd pythontree
		$ python setup.py install
		```
* ### Roots ###
	* roots
		it's a grapich function, print a tree of the chosen path
		```
		import pythontree
		Roots = pythontree.Roots('*** you can choose the path to start ***')
		Roots.roots()
		```
		![Alt text](https://raw.githubusercontent.com/MattVoid/pythontree/master/img/roots.jpg?raw=true)
	* element
		return an array with files or folders starting from your chosen path
		```
		import pythontree
		Roots = pythontree.Roots('*** you can choose the path to start ***')
		Roots.element()[0] #return files
		Roots.element()[1] #return folders
		```
* ### Clean ###
  	* element
		* grapich mode off
			return an array with empty folder or equal file 
			```
			import pythontree
			Clean = pythontree.Clean('*** you can choose the path to start ***')
			Clean.element() #Clean.element('off')
			Clean.element()[0] #empty folders
			Clean.element()[1] #equals files
			```
		* graphic mode on
			print path of equal file and empty folder starting from your chosen path
			```
			import pythontree
			Clean = pythontree.Clean('*** you can choose the path to start ***').element(on)
			Clean.element('on')
			```
		![Alt text](https://raw.githubusercontent.com/MattVoid/pythontree/master/img/clean.jpg?raw=true)
