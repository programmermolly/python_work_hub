# 父类
class User:
	"""用于打印用户信息"""
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print(self.first_name,self.last_name)
	def greet_user(self):
		print(f'Hello,{self.first_name}')

# 子类
class Admin(User):
	"""显示管理员权限"""
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.previleges=[]
	def show_previleges(self):
		for previlege in self.previleges:
			print(previlege)

# 创建实例
admin=Admin('Peter','Jiang')
admin.previleges=['can add post','can delete post','can ban user']
admin.show_previleges()