import unittest
from unittest.mock import patch
from real import UsingMicroInProd, other_important_func
import micro

class TestingRealCode(unittest.TestCase):
    
    def test_important(self):
        # with patch('name of the thing i am patching', return_value='the desired result')
        with patch('micro.plus', return_value=4):  
            #Arrange--have your SetUp inside the mthod
            production = UsingMicroInProd()

            #Act        return "Answer: {}".format(micro.plus(operand1, operand2))
            expected_result = "Answer: {}".format(4)
            actual_result = production.important(2, 2)

            #Assert
            self.assertEquals(expected_result, actual_result)

    def test_other_important(self):
        with patch('micro.plus', return_value=4):
            #Arrange (not mandatory see note above)

            #Act
            expected_result = "Answer: {}".format(4)
            actual_result = other_important_func()

            #Assert
            self.assertEquals(expected_result, actual_result)

    def test_important_fails_when_plus_returns_negative(self):
        with patch('micro.plus', side_effect=ValueError('Does not work')):

            #Arrange
            prod = UsingMicroInProd()

            #Act
            with self.assertRaises(ValueError):
                prod.important(-1, -2)








# run 'python -m unittest test'






