import unittest
from app import CalculatorApp

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()

    def test_add(self):
        res = self.app.add(1, 2)
        self.assertEqual(res, 3)

    def test_subtract(self):
        res = self.app.subtract(1, 2)
        self.assertEqual(res, -1)

    def test_multiply(self):
        res = self.app.multiply(3, 10)
        self.assertEqual(res, 3)

    def test_power(self):
        res = self.app.power(2, 4)
        self.assertEqual(res, 16)
