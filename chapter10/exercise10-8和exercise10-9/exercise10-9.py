try:
	with open('cats.txt') as c:
		res=c.read()
except FileNotFoundError:
	pass
else:
	print(res)


try:
	with open('dogs.txt') as d:
		res1=d.read()
except FileNotFoundError:
	pass
else:
	print(res1)