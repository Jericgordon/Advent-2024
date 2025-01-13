import unittest
from day_6 import part_one,part_two

class day_5_tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(41,part_one("Tests/day_6_test.txt"))

    def test_part_two(self):
        ...

if __name__ == "__main__":
    unittest.main()
