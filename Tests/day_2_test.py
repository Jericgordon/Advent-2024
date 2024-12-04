import unittest
from day_2 import part_one,part_two,checks_two_values,level_checker,safe_level_checker


class Checker_tests(unittest.TestCase):
    def two_values_test(self):
        self.assertTrue(checks_two_values(7,5,1))
        self.assertFalse(checks_two_values(5,7,1))
        self.assertTrue(checks_two_values(5,7,-1))
        self.assertFalse(checks_two_values(7,5,-1))
        self.assertFalse(checks_two_values(9,5,-1))
        self.assertFalse(checks_two_values(3,8,1))

