usr_names=['Mary','Lily','Simon','admin']
# 测试程序时用的代码，如不需要测试，请保持原状，以免影响程序的运行
# usr_names.pop()
# usr_names.pop()
# usr_names.pop()
# usr_names.pop()
if usr_names:
	for usr_name in usr_names:
		if usr_name=='admin':
			print('Hello admin,would you like to see a status report?')
		else:
			print(f'Hello {usr_name},thank you for logging in again')
		
else:
	print('We need to find some users!')




