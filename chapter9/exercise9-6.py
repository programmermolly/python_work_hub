# 父类
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)

	def open_restaurant(self):
		print('The restaurant is open') # 餐馆正在营业

	def set_number_served(self,new_number):
		self.number_served=new_number

	def increment_number_served(self,add_number):
		self.number_served+=add_number



# 子类
class IceCreamStand(Restaurant):
	'''描述小店'''
	def __init__(self,name,cuisine_type='icecream'):
		super().__init__(name,cuisine_type)
		self.flavours=[]
	def print_icecream(self):
		for flavour in self.flavours:
			print(flavour)


# 创建实例
icecreamstand=IceCreamStand('清凉冰激凌店')
icecreamstand.flavours=['草莓味','哈密瓜味','芒果味']
icecreamstand.print_icecream()
icecreamstand.describe_restaurant()

