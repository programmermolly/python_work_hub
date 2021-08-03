with open('红楼梦第一回.txt',encoding='UTF-8') as f:
	res=f.read()
num=res.count('红')
print(num)