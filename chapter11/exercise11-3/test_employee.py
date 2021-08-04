import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.first_name='Xin'
		self.last_name='Jiang'
		self.salary=3500
		self.employee=Employee(self.first_name,self.last_name,self.salary)
	def test_give_default_raise(self):
		final_salary=self.employee.give_raise()
		self.assertEqual(final_salary,8500)
	def test_give_custom_raise(self):
		final_salary=self.employee.give_raise(3000)
		self.assertEqual(final_salary,6500)
if __name__ == '__main__':
	unittest.main()
		