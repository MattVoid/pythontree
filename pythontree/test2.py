from Element import Element

e = Element("/Users/matt/Desktop/Project/python/pythontree/pythontree/prova.py")
print(e.name)
print(e.path)
print(e.type)
print(e.is_dir)
print(e.is_file)

print()

e.path = "/Users/matt/Desktop/Project/python/pythontree/pythontree/Element"
print(e.name)
print(e.path)
print(e.type)
print(e.is_dir)
print(e.is_file)
