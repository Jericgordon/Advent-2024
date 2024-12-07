import unittest
from day_2 import part_one,part_two,checks_two_values,level_checker,safe_level_checker,find_sign,brute_force_helper


class checker_tests(unittest.TestCase):
    def test_two_values(self):
        self.assertTrue(checks_two_values(7,5,1))
        self.assertFalse(checks_two_values(5,7,1))
        self.assertTrue(checks_two_values(5,7,-1))
        self.assertFalse(checks_two_values(7,5,-1))
        self.assertFalse(checks_two_values(9,5,-1))
        self.assertFalse(checks_two_values(3,8,1))
    def test_case_2(self):
        self.assertFalse(safe_level_checker([38, 45, 48, 49, 52, 53, 54, 54]))
        

    def test_case_3(self):
        self.assertTrue(safe_level_checker([31, 32, 30, 33, 34, 37]))
        self.assertTrue(safe_level_checker([45, 48, 49, 52, 53, 54, 54]))
    
    def test_case_4(self): #fixthis
        self.assertFalse(safe_level_checker([36, 39, 41, 43, 44, 41, 44]))

    def test_case_5(self):
        self.assertTrue(safe_level_checker([16, 18, 19, 20, 23]))
    

    def test_sign(self):
        test1 = [31, 32, 30, 33, 34, 37]
        test2 = [45, 48, 49, 52, 53, 54, 54]
        test3 = [38, 45, 48, 49, 52, 53, 54, 54]
        self.assertEqual(-1,find_sign(test1[:4]))
        self.assertEqual(-1,find_sign(test2[:4]))
        self.assertEqual(-1,find_sign(test3[:4]))
    def test_bf(self):
        self.assertTrue(brute_force_helper([35, 37, 38, 41, 43, 41]))