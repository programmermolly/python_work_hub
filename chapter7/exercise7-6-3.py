# 使用break退出循环
age=''
while age!='quit':
	age=input('请输入您的年龄： ')
	if age=='quit':
		break
	# 输入不是"quit"时，进入条件判断，确定票价
	else:
		age=int(age)
		if int(age)<3:
			print('Free!')
		elif int(age)<=12:
			print('10$please!')
		
		else:
			print('15$please')
		