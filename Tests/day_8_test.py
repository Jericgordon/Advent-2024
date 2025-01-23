from day_8 import *
import unittest

class day_5_tests(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(14,part_one("Tests/day_8_test.txt"))
       
    def test_part_two(self):
        self.assertEqual(34,part_two("Tests/day_8_test.txt"))