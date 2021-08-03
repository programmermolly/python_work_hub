import unittest
from city_functions import city_country
class LocationTestCase(unittest.TestCase):
	"""函数测试用例"""
	def test_city_country(self):
		full_location=city_country('Santigo','Chile')
		self.assertEqual(full_location,'Santigo,Chile-population None')
if __name__ == '__main__':
	unittest.main()
		

