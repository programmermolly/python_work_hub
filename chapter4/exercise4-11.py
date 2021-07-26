pizzas=['Raspberry sesame ham pizza','Cheese macaroni pizza','Pumpkin cheese crispy pizza','Buffalo Chicken Pizza']
for pizza in pizzas:
	print(pizza)
for pizza in pizzas:
	print(pizza)
for pizza in pizzas:
	print(f'I like {pizza}')
print('\nI really love pizza')

friend_pizzas=pizzas[:]

friend_pizzas.append('Hawaii Pizza')

print('原列表为',pizzas)
print('副本为：',friend_pizzas)
print('\n\n')

print('My favourite pizzas are:')
for p1 in pizzas:
	print(p1)
print('\n\n')

print("My freind's favourite pizzas are:")
for p2 in friend_pizzas:
	print(p2)
