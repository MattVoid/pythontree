import os
import pythontree
path = input('choose the path to clean: ')
x = 1
file = ''
dir = ''
check = pythontree.Clean(path).element()
for i in range(len(check[0])):
	print(str(x) + ' - ' + check[0][i] + "\033[1;31m" + ' is empty!' + "\033[0;0m")
	dir = dir + ''.join(str(x - 1) + '-')
	x = x + 1
for i in range(len(check[1])):
	print(str(x) + ' - ' + check[1][i] + "\033[1;31m" + ' is equal to ' + "\033[0;0m" + check[2][i])
	file = file + ''.join(str(x - 1) + '-')
	x = x + 1
print('what do you want to delete?')
if check[0]:
	print('1) Empty folders')
if check[2]:
	print('2) Equal files')
if check[0] and check[2]:
	print('3) Both')
print('4) Exit')
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
elif choose == '4':
	print("\033[1;32m" + 'No things was deleted!' + "\033[0;0m")
	exit()
else:
	print('\033[1;93m' + 'Choice not available!' + "\033[0;0m")
	exit()