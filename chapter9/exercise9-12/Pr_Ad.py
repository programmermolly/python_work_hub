from User import User
class Admin(User):
	"""显示管理员权限"""
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privilege =Privileges()
	

class Privileges:
	"""将类进行拆分"""
	def __init__(self):
		self.privileges=[]
	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)	
