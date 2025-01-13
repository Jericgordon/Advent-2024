import unittest
from day_5 import part_one,part_two

class day_5_tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(143,part_one("Tests/day_5_test.txt"))

    def test_part_two(self):
        self.assertEqual(123,part_two("Tests/day_5_test.txt"))

if __name__ == "__main__":
    unittest.main()

        