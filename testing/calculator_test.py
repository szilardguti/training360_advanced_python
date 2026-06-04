"""
calculator - module
Calculator - class
    sum(a,b) -> int : sum of a and b
"""

import unittest
from calculator import Calculator


class BasicCalcTests(unittest.TestCase):
    def test_sum_of_two(self):
        calc = Calculator()
        result = calc.sum(2, 3)

        self.assertEqual(5, result)

    def test_diff_of_two(self):
        calc = Calculator()
        result = calc.diff(10, 2)

        self.assertEqual(8, result)

    def test_prod_of_two(self):
        calc = Calculator()
        result = calc.product(3, 7)

        self.assertEqual(21, result)

    def test_power(self):
        calc = Calculator()
        result = calc.power(3, 3)

        self.assertEqual(27, result)

    def test_prod_of_three(self):
        calc = Calculator()
        result = calc.product(2, 2, 3, 4)

        self.assertEqual(48, result)
