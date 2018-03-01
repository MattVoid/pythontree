import os
import pythontree
path = input('choose the path to clean: ')
x = 1
file = ''
dir = ''
check = pythontree.Clean(path).element()
for i in range(len(check[0])):
	print(str(x) + ' - ' + check[0][i] + "\033[1;31m" + ' is empty!' + "\033[0;0m")
	dir = dir + ''.join(str(x - 1))
	x = x + 1
for i in range(len(check[1])):
	print(str(x) + ' - ' + check[1][i] + "\033[1;31m" + ' is equal to ' + "\033[0;0m" + check[2][i])
	file = file + ''.join(str(x - 1))
	x = x + 1
print('what do you want to delete?')
if check[0]:
	print('1) Empty folders')
if check[2]:
	print('2) Equal files')
if check[0] and check[2]:
	print('3) Both')
if check[0] or check[2]:
	print('4) Choose what delete')
print('5) Exit')
choose = input('choose: ')
if choose == '1' and check[0]:
	pythontree.Clean(path).delete('dirs')
	for i in range(len(check[0])):
		print(check[0][i] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
elif choose == '2' and check[1]:
	pythontree.Clean(path).delete('files')
	for i in range(len(check[1])):
		print(check[1][i] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
elif choose == '3' and check[0] and check[1]:
	pythontree.Clean(path).delete('both')
	for i in range(len(check[0])):
		print(check[0][i] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
	for i in range(len(check[2])):
		print(check[2][i] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
elif choose == '4' and check[0] or check[1]:
	delete = input('choose the files or folders to delete: ').replace(' ', '')
	if ';' in delete:
		delete = delete.split(';')
		for x in range(len(delete)):
			if '-' in delete[x]:
				loop = delete[x].split('-')
				for i in range(int(loop[0]), int(loop[1]) + 1):
					if str(i - 1) in dir:
						os.rmdir(check[0][i - 1])
						print(check[0][i - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
					elif str(i - 1) in file:
						os.remove(check[2][i - 1])
						print(check[2][i - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
					else:
						print(loop[i] + ' - ' + '\033[1;93m' + 'Element not found!' + "\033[0;0m")
			else:
				if str(int(delete[x])) in dir:
					os.rmdir(check[0][int(delete[x])])
					print(check[0][int(delete[x])] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
				elif str(int(delete[x])) in file:
					os.remove(check[1][int(delete[x])])
					print(check[1][int(delete[x])] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
				else:
					print(delete[x] + ' - ' + '\033[1;93m' + 'Element not found!' + "\033[0;0m")
	else:
		if '-' in delete:
			delete = delete.split('-')
			for i in range(int(delete[0]), int(delete[1]) + 1):
				if str(i - 1) in dir:
					os.rmdir(check[0][i - 1])
					print(check[0][i - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
				elif str(i - 1) in file:
					os.remove(check[1][i - 1])
					print(check[1][i - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
				else:
					print(delete[i] + ' - ' + '\033[1;93m' + 'Element not found!' + "\033[0;0m")
		else:
			if str(int(delete) - 1) in dir:
				os.rmdir(check[0][int(delete) - 1])
				print(check[0][int(delete) - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
			elif str(int(delete) - 1) in file:
				os.remove(check[1][int(delete) - 1])
				print(check[1][int(delete) - 1] + "\033[1;31m" + ' was deleted!' + "\033[0;0m")
			else:
				print(delete + ' - ' + '\033[1;93m' + 'Element not found!' + "\033[0;0m")
elif choose == '5':
	print("\033[1;32m" + 'No things was deleted!' + "\033[0;0m")
	exit()
else:
	print('\033[1;93m' + 'Choice not available!' + "\033[0;0m")
	exit()'''
