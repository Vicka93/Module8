"""
Author:Viktoria Denys
Program:set_membership.py
"""
import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    # assertion for an item in the set (expect True)
    def test_in_set_true(self):
        my_set = {1, 3, 8}
        my_val = 8
        self.assertEqual(True, set_membership.in_set(my_set, my_val))

    # One assertion for an item not in the set (expect False)
    def test_in_set_false(self):
        my_set = {1, 3, 8}
        my_val = 5
        self.assertEqual(False, set_membership.in_set(my_set, my_val))


if __name__ == '__main__':
    unittest.main()
