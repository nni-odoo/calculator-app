import unittest
from app import CalculatorApp

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()

    def test_add(self):
        res = self.app.add(1, 2)
        self.assertEqual(res, 3)

    def test_sbutract(self):
        res = self.app.subtract(1, 2)
        self.assertEqual(res, -1)
