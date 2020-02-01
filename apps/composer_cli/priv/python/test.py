import os, unittest

from .proc import *

gridbad = {(1, 1): 1, (1, 2): 1}

gridok1 = {(1, 2): 3, (2, 3): 4}

gridok2 = { # from Extreme Sudoku 73 p.9, puzzle 11
    (1, 4): 7, (1, 8): 1, (1, 9): 6,
    (2, 2): 9, (2, 3): 5, (2, 4): 3, (2, 7): 7, (2, 8): 8,
    (3, 7): 3,
    (4, 1): 5, (4, 3): 2, (4, 5): 3,
    (5, 4): 5, (5, 5): 7,
    (6, 1): 1, (6, 3): 6, (6, 5): 9,
    (7, 7): 5,
    (8, 2): 3, (8, 3): 7, (8, 4): 2, (8, 7): 8, (8, 8): 6,
    (9, 4): 4, (9, 8): 3, (9, 9): 1,
}

solution2 = {
    (4, 4): (1, 'answer'), (1, 6): (8, 'answer'), (2, 9): (2, 'answer'),
    (6, 1): (1, 'question'), (5, 4): (5, 'question'), (3, 4): (6, 'answer'),
    (3, 1): (7, 'answer'), (8, 7): (8, 'question'), (9, 8): (3, 'question'),
    (2, 1): (6, 'answer'), (8, 1): (4, 'answer'), (9, 3): (9, 'answer'),
    (9, 9): (1, 'question'), (5, 7): (1, 'answer'), (4, 9): (7, 'answer'),
    (3, 3): (8, 'answer'), (2, 5): (4, 'answer'), (1, 2): (2, 'answer'),
    (3, 6): (9, 'answer'), (3, 5): (2, 'answer'), (8, 9): (9, 'answer'),
    (7, 5): (8, 'answer'), (4, 8): (9, 'answer'), (6, 3): (6, 'question'),
    (5, 9): (8, 'answer'), (6, 7): (4, 'answer'), (2, 4): (3, 'question'),
    (5, 6): (6, 'answer'), (6, 5): (9, 'question'), (5, 2): (4, 'answer'),
    (4, 1): (5, 'question'), (2, 6): (1, 'answer'), (8, 6): (5, 'answer'),
    (2, 2): (9, 'question'), (2, 7): (7, 'question'), (3, 7): (3, 'question'),
    (9, 4): (4, 'question'), (3, 9): (5, 'answer'), (1, 4): (7, 'question'),
    (8, 5): (1, 'answer'), (6, 4): (8, 'answer'), (3, 8): (4, 'answer'),
    (8, 2): (3, 'question'), (7, 4): (9, 'answer'), (7, 7): (5, 'question'),
    (5, 1): (9, 'answer'), (4, 2): (8, 'answer'), (7, 8): (7, 'answer'),
    (7, 1): (2, 'answer'), (7, 9): (4, 'answer'), (1, 3): (4, 'answer'),
    (6, 8): (5, 'answer'), (8, 3): (7, 'question'), (9, 6): (7, 'answer'),
    (2, 8): (8, 'question'), (4, 7): (6, 'answer'), (8, 4): (2, 'question'),
    (3, 2): (1, 'answer'), (2, 3): (5, 'question'), (6, 2): (7, 'answer'),
    (9, 1): (8, 'answer'), (7, 6): (3, 'answer'), (1, 1): (3, 'answer'),
    (1, 8): (1, 'question'), (9, 7): (2, 'answer'), (6, 9): (3, 'answer'),
    (1, 9): (6, 'question'), (7, 3): (1, 'answer'), (1, 7): (9, 'answer'),
    (9, 2): (5, 'answer'), (5, 3): (3, 'answer'), (5, 8): (2, 'answer'),
    (7, 2): (6, 'answer'), (1, 5): (5, 'answer'), (4, 3): (2, 'question'),
    (8, 8): (6, 'question'), (4, 5): (3, 'question'), (9, 5): (6, 'answer'),
    (6, 6): (2, 'answer'), (5, 5): (7, 'question'), (4, 6): (4, 'answer')
}

class TestProc(unittest.TestCase):
    def setUp(self):
        dirn = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        rfn = 'asp/sudoku9.lp'
        self.rules_fn = bytes(os.path.join(dirn, rfn), 'utf-8')

    def test_maybe_solution_ok(self):
        grid = gridok2
        (label, grout) = maybe_solution(grid, self.rules_fn)
        self.assertEqual(label, 'ok', 'incorrect label')
        self.assertEqual(sorted(grout.items()), sorted(solution2.items()),
                         'incorrect solution')

    def test_maybe_solution_bad(self):
        grid = gridbad
        (label, grout) = maybe_solution(grid, self.rules_fn)
        self.assertEqual(label, 'error', 'incorrect label')
        self.assertEqual(list(grout.items()), [], 'incorrect solution')

    def test_maybe_valid_grid_ok(self):
        grid = gridok1
        (label, message) = maybe_valid_grid(grid, self.rules_fn)
        self.assertEqual(label, 'ok', 'incorrect label')
        self.assertEqual(message, '100+ solutions found.', 'incorrect message')

    def test_maybe_valid_grid_bad(self):
        grid = gridbad
        (label, message) = maybe_valid_grid(grid, self.rules_fn)
        self.assertEqual(label, 'error', 'incorrect label')
        self.assertEqual(message, 'No solutions found.', 'incorrect message')

if __name__ == '__main__':
    unittest.main()
