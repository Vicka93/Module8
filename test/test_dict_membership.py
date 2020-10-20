import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    # assertion for an item in the dictionary (expect True)
    def test_in_set_true(self):
        my_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        my_val = 'A'
        self.assertEqual(True, dict_membership.in_dict(my_dict, my_val))

    # One assertion for an item not in the dictionary (expect False)
    def test_in_set_false(self):
        my_dict = my_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        my_val = 'J'
        self.assertEqual(False, dict_membership.in_dict(my_dict, my_val))


if __name__ == '__main__':
    unittest.main()
