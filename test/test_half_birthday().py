"""
Author:Viktoria Denys
Program:half_birthday.py
function to compute a half birthday.
"""
import unittest
from datetime import datetime
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime(2020, 9, 29)
        self.assertEqual(datetime(2021, 3, 29), half_birthday.half_birthday(birthday))


if __name__ == '__main__':
    unittest.main()
