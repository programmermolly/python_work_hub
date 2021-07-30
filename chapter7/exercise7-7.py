# 这是一个无限循环，请在终端运行，按Ctrl+C退出
age=input('请输入您的年龄： ')
while age!='quit':

	# 输入不是"quit"时，进入条件判断，确定票价
		age=int(age)
		if int(age)<3:
			print('Free!')
		elif int(age)<=12:
			print('10$please!')
		
		else:
			print('15$please')