class User:
	"""用于打印用户信息"""
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	def describe_user(self):
		print(self.first_name,self.last_name)
	def greet_user(self):
		print(f'Hello,{self.first_name}')
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0


# 创建实例
usr=User('敏','李')
usr.increment_login_attempts()
usr.increment_login_attempts()
usr.increment_login_attempts()
print(usr.login_attempts)

# 重置登陆次数
usr.reset_login_attempts()
print(usr.login_attempts)

		