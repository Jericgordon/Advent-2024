from day_7 import importdoc,part_one
import unittest

class day_5_tests(unittest.TestCase):
    def test_import_doc(self):
        importdoc("Tests/day_7_test.txt")

    def test_part_one(self):
        self.assertEqual(3749,part_one("Tests/day_7_test.txt"))
       
    def test_part_two(self):
        ...