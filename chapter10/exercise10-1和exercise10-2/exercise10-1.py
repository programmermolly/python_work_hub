# 第一次打印
with open('learning_python.txt') as file_object:
	contents=file_object.read()
	print(contents)
# 第二次打印
with open('learning_python.txt') as file_object:
	for line in file_object:
		print(line)

# 第三次打印
file_name='learning_python.txt'
with open(file_name) as file_object:
	lines=file_object.readlines()

for line in lines:
	print(line)   