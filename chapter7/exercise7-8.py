# 三明治=['金枪鱼三明治','火腿奶酪三明治','水果三明治']
sandwich_orders=['tuna sandwich','Ham and cheese sandwich','Fruit sandwich']
finished_sandwiches=[]
while sandwich_orders:
	made_sandwich=sandwich_orders.pop()
	print(f'I made your {made_sandwich}')
	finished_sandwiches.append(made_sandwich) 
print('\n')

# 将所有三明治列出来
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)