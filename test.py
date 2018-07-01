import unittest
from req import *

class TestTesting(unittest.TestCase):

    def test_cheese(self):
        self.assertEqual(calculate_cheese(19.99, 3.24, 0.7572, 0.854445), 6)



    def test_cheese_2(self):
        self.assertEqual(calculate_cheese(500, 18.45, 0.7572, 0.854445), 30)



    def test_cheese_3(self):
        self.assertEqual(calculate_cheese(64.67, 2.54, 0.7572, 0.854445), 28)



    def test_convert(self):
        self.assertEqual(convert(10, 2), 5)



if __name__ == '__main__':
    unittest.main()
