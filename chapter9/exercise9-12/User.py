class User:
	"""用于打印用户信息"""
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print(self.first_name,self.last_name)
	def greet_user(self):
		print(f'Hello,{self.first_name}')