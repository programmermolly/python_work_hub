active=True
while active:
	name=input('请输入您的名字(输入"q"退出)： ')
	if name!='q':
		with open('guest_book.txt','a') as file_object:
			file_object.write(f'{name}\n')
	else:
		break
	

	