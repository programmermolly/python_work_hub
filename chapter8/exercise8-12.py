def add_toppings(*toppings):
	for topping in toppings:
		print(f'In this sandwich,there are {topping}')


# 函数调用

add_toppings('ham')

add_toppings('ham','cheese')

add_toppings('ham','cheese','vegetables')