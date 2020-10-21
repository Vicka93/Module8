import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    # test function pass for key value of 'A'
    def test_A(self):
        self.assertEqual("You entered an A", assign_average.switch_average('A'))

    # test function pass for key value of 'a', upper() added to switch_average
    def test_a(self):
        self.assertEqual("You entered an A", assign_average.switch_average('a'))

    # test function pass for key value of 'B'
    def test_B(self):
        self.assertEqual("You entered an B", assign_average.switch_average('B'))

    # test function pass for key value of 'C'
    def test_C(self):
        self.assertEqual("You entered an C", assign_average.switch_average('C'))

    # test function pass for key value of 'D'
    def test_D(self):
        self.assertEqual("You entered an D", assign_average.switch_average('D'))

    # test function pass for key value of 'F'
    def test_F(self):
        self.assertEqual("You entered an F", assign_average.switch_average('F'))

    # test function pass for non_key value
    def test_non_key(self):
        self.assertEqual("R is not a valid Grade", assign_average.switch_average('R'))


if __name__ == '__main__':
    unittest.main()
