from unittest import TestCase, mock
from Unit_Test.Calculator import Calculator

class TestCalculator(TestCase):
    @mock.patch('Unit_Test.Calculator.Calculator.sum_numbers', return_value = 8)

    def test_sum_numbers(self, mock_sum_numbers):
        sumo = Calculator(2,4)
        print(sumo.sum_numbers())
        self.assertEqual(sumo.sum_numbers(), 8)

