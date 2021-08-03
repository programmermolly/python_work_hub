num1=input('请输入第一个数： ')
num2=input('请输入第二个数： ')
try:
	res=int(num1)+int(num2)
except ValueError:
	print('请输入一个数字！')
else:
	print(f'{num1}+{num2}={res}')


