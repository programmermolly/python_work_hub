class User:
	"""用于打印用户信息"""
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print(self.first_name,self.last_name)
	def greet_user(self):
		print(f'Hello,{self.first_name}')

# 创建实例

user1=User('鑫','姜')
user2=User('敏','李')
user3=User('亦凡','吴')

# 调用方法
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()