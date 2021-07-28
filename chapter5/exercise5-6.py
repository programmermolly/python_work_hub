# python中可以把多个不等式连在一起写，和手写一样.不需要用and
age=20
if age<2:
	print('You are a baby')
elif 2<=age<4:
	print('You are an infant') # 你是幼儿
elif 4<=age<13:
	print('You are a child')
elif 13<=age<20:			   
	print('You are a teenager')
elif 20<=age<65:
	print('You are an adult')
else:
	print('You are an old man')

