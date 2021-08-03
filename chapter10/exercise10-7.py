print('这是一个加法计算器，如果要退出，请输入“q”')
while True:
	num1=input('请输入第一个数： ')
	if num1=='q':
		break
	num2=input('请输入第二个数： ')
	if num2=='q':
		break  
	try:
		res=int(num1)+int(num2)
	except ValueError:
		print('请输入一个数字！')
	else:
		print(f'{num1}+{num2}={res}')

