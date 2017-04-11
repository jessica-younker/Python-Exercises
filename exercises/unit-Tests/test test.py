import unittest
# calculator.py is module, Calculator will be class in that module
from calculator import Calculator

class TestCalculationMethods(unittest.TestCase):

	def test_add(self):
		calculater = Calculator()
		self.assertEqual(calculator.add(2,2), 4)

	def test_subtract(self):
		calculater = Calculator()
		self.assertEqual(calculator.subtract(2,2), 0)

	def test_multiply(self):
		calculater = Calculator()
		self.assertEqual(calculator.multiply(2,3), 6)

	def test_divide(self):
		calculater = Calculator()
		self.assertEqual(calculator.divide(10, 5), 2)


if __name__ == '__main__':
    unittest.main()




#test to make sure tests fail....methods may exist in code, and you don't realize it