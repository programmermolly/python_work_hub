try:
	with open('cats.txt') as c:
		res=c.read()
except FileNotFoundError:
	print('文件不存在！')
else:
	print(res)


try:
	with open('dogs.txt') as d:
		res1=d.read()
except FileNotFoundError:
	print('文件不存在！')
else:
	print(res1)