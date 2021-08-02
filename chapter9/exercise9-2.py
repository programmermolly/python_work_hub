class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)
	def open_restaurant(self):
		print('The restaurant is open') # 餐馆正在营业
# 创建实例
restaurant=Restaurant('花园饭店','比萨')
print(f"The restaurant's name is {restaurant.restaurant_name} ")
print(f'Cuisine_type is {restaurant.cuisine_type}')
restaurant.describe_restaurant()

restaurant2=Restaurant('杨氏大酒店','烤鸭')
restaurant2.describe_restaurant()

restaurant3=Restaurant('北京国际酒店','西餐')
restaurant3.describe_restaurant()