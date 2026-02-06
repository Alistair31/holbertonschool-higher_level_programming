#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def tests(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-1, -5, -3]), -1)
        self.assertEqual(max_integer([10]), 10)
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
