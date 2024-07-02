import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        self.assertEqual(
        m1._cells[1][1]._visited,
        False
        )

if __name__ == "__main__":
    unittest.main()
