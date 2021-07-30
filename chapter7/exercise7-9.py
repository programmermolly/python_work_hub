print('Pastrami is over!')
sandwich_orders=['pastrami','tuna sandwich','pastrami','Ham and cheese sandwich','Fruit sandwich','pastrami']

# 删除pastrami
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

# 验证是否全部删除
print(sandwich_orders)
