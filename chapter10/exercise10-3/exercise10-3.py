name=input('请输入您的名字：')
with open('guest.txt','w') as file_object:
	file_object.write(name)