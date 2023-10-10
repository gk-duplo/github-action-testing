# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 7)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calculator.multiply(5, 2)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = self.calculator.divide(12, 3)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(8, 0)


if __name__ == '__main__':
    unittest.main()
