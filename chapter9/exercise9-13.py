from random import randint
class Die:
	"""掷骰子"""
	def __init__(self):
		
		self.sides = 6
	def roll_die(self):
		num=randint(1,self.sides)
		print(num)

# 创建6面的骰子
die=Die()
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	
die.roll_die()	