import unittest
from day_3 import part_one

class day_3_tests(unittest.TestCase):
    
    def test_given(self):
        testcase = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(161,part_one(testcase))
        
