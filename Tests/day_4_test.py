import unittest
from day_4 import Word_search_solver
class day_4_tests(unittest.TestCase):
    def test_part_one(self):
        input = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],['M','X','M','X','A','X','M','A','S','X']]
        w = Word_search_solver()
        self.assertEqual(18,w.part_one(input))

    def test_get_next_letter(self): #xmas, 
        w = Word_search_solver()
        self.assertEqual("A",w.get_next_letter(-1))
        self.assertEqual("M",w.get_next_letter(1))

    def test_right_diagonal(self):
        test_input = [['X', 'B', 'B', 'B'], ['B', 'M', 'B', 'B'], ['B', 'B', 'A', 'B'], ['B', 'B', 'B', 'S']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_left_diagonal(self):
        test_input = [['B', 'B', 'B', 'X'], ['B', 'B', 'M', 'B'], ['B', 'A', 'B', 'B'], ['S', 'B', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))


    def test_horizontal(self):
        test_input = [['B', 'B', 'B', 'B'], ['X', 'M', 'A', 'S'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_vertical(self):
        test_input = [['B', 'X', 'B', 'B'], ['B', 'M', 'B', 'B'], ['B', 'A', 'B', 'B'], ['B', 'S', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_backwards_vertical(self):
        test_input = [['B', 'S', 'B', 'B'], ['B', 'A', 'B', 'B'], ['B', 'M', 'B', 'B'], ['B', 'X', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_backwards_horizontal(self):
        test_input = [['B', 'B', 'B', 'B'], ['S', 'A', 'M', 'X'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_backwards_right_diagonal(self):
        test_input = [['S', 'B', 'B', 'B'], ['B', 'A', 'B', 'B'], ['B', 'B', 'M', 'B'], ['B', 'B', 'B', 'X']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_backwards_left_diagonal(self):
        test_input = [['B', 'B', 'B', 'S'], ['B', 'B', 'A', 'B'], ['B', 'M', 'B', 'B'], ['X', 'B', 'B', 'B']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_one(test_input))

    def test_double_horisontal(self):
        test_input = [['B', 'B', 'B', 'B', 'B', 'B', 'B'], ['X', 'M', 'A', 'S', 'A', 'M', 'X'], ['B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B']]        
        w = Word_search_solver()
        self.assertEqual(2,w.part_one(test_input))

    def test_simple(self):
        test_input = [['.', '.', 'X', '.', '.', '.'], ['.', 'S', 'A', 'M', 'X', '.'], ['.', 'A', '.', '.', 'A', '.'], ['X', 'M', 'A', 'S', '.', 'S'],['.','X','.','.','.','.']]
        w = Word_search_solver()
        self.assertEqual(4,w.part_one(test_input)) 

    def test_part_two_simple(self):
        test_input = [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']]
        w = Word_search_solver()
        self.assertEqual(1,w.part_two(test_input))

    def test_part_two_complex(self):
        test_input = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],['M','X','M','X','A','X','M','A','S','X']]
        w = Word_search_solver()
        self.assertEqual(9,w.part_two(test_input))