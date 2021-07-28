usr_names=['Mary','Lily','Simon','admin']
for usr_name in usr_names:
	if usr_name=='admin':
		print('Hello admin,would you like to see a status report?')
	else:
		print(f'Hello {usr_name},thank you for logging in again')
	
	