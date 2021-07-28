current_users=['Mary','Lily','Simon','Alex','Bob']
new_users=['Mary','Lily','Rax','Peter','Owen']
current_users_copy=[current_user.lower() for current_user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users_copy:
		print('You have to input an another user name!')
	else:
		print('This user name is not used!')