pizzas=['Raspberry sesame ham pizza','Cheese macaroni pizza','Pumpkin cheese crispy pizza']
friend_pizzas=pizzas[:]

pizzas.append('Buffalo Chicken Pizza') # 布法罗鸡肉披萨块
friend_pizzas.append('Hami melon pine nut pizza') # 哈密瓜松子披萨

print('My favourite pizzas are:')

for pizza1 in pizzas:
	print(pizza1)

print("My friend's favourite pizzas are:")

for pizza2 in pizzas:
	print(pizza2)