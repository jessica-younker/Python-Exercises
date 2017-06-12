import unittest
from unittest.mock import patch
from real import UsingMicroInProd, another_important_func
import micro


class TestingRealCode(unittest.TestCase):

    def test_important(self):
        with patch('micro.plus', return_value=4):

            '''
            Python did:
            def plus(operand1, operand2):
                return 4
            '''
            # Arrange
            production = UsingMicroInProd()

            # Act
            expected_result = "Answer: {}".format(4)
            actual_result = production.important(2, 2)

            # Assert
            self.assertEquals(expected_result, actual_result)

    def test_other_important(self):
        with patch('micro.plus', return_value=4):
            # Arrange

            # Act
            expected_result = "Answer: {}".format(4)
            actual_result = another_important_func()

            # Assert
            self.assertEquals(expected_result, actual_result)

    def test_important_fails_when_plus_returns_negative(self):

        with patch('micro.plus', return_value=-1):
            # Arrange
            prod = UsingMicroInProd()

            # Act
            with self.assertRaises(ValueError):
                prod.important(-1, -2)

    def test_important_fails_when_plus_raises_exception(self):

        with patch('micro.plus', side_effect=ValueError):
            # Arrange
            prod = UsingMicroInProd()

            # Act
            expected_result = "Plus method failed for undefined reason"
            actual_result = prod.important(-1, -2)

            # Assert
            self.assertEquals(expected_result, actual_result)
