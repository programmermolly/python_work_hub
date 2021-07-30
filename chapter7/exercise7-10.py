print('If you could visit one place in the world,where would you go?')
print('Welcome to our survey!')

responses={}
active=True
while  active:

	name=input('Please input your name: ')
	response=input('Please input your ideal place: ')

	responses[name]=response
	print('\n')
	repeat=input('Do you want to be interviewed?(Yes/No)')
	if repeat=='No':
		active=False
print('Thank you for participation!')


# 打印调查结果
for name,place in responses.items():
	print(f'{name}:{place}')
