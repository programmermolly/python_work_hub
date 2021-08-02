print('下面请输入你喜欢编程的原因（输入“q”退出）')
active=True
while active:
	reason=input('输入你喜欢编程的原因： ')
	if reason!='q':
		with open('reasons.txt','a') as file_object:
			file_object.write(f'我之所以喜欢编程，是因为{reason}\n')
	else:
		break

	
