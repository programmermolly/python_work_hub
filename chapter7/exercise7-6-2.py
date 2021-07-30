# 使用active控制循环
active=True  
while active:
	age=input('请输入您的年龄： ')
	if age=='quit':
		active=False
	else:
		age=int(age)
		if int(age)<3:
			print('Free!')
		elif int(age)<=12:
			print('10$please!')
		
		else:
			print('15$please')
		