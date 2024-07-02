from cell import Cell
import time, random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if seed: self._seed = random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(random.randint(0, num_cols - 1), random.randint(0, num_rows - 1))
        self._reset_cells_visited()

    def _create_cells(self):
        if self._num_rows == 0: raise Exception("Must at least have one row")
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows): column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])): self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._win: return
        x1, y1 = self._x1 + self._cell_size_x * i, self._y1 + self._cell_size_y * j
        x2, y2 = self._x1 + self._cell_size_x * (i + 1), self._y1 + self._cell_size_y * (j + 1)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win: return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[-1]) - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            adjacent = []
            if i > 0: adjacent.append((i - 1, j))
            if i < self._num_cols - 1: adjacent.append((i + 1, j))
            if j > 0: adjacent.append((i, j - 1))
            if j < self._num_rows - 1: adjacent.append((i, j + 1))
            not_visited = []
            for cell in adjacent:
                if not self._cells[cell[0]][cell[1]]._visited: not_visited.append(cell)
            if not not_visited: self._draw_cell(i, j); return
            index = random.choice(not_visited)
            if index[0] < i:
                self._cells[index[0]][index[1]].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            elif index[0] > i:
                self._cells[index[0]][index[1]].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            elif index[1] < j:
                self._cells[index[0]][index[1]].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            elif index[1] > j:
                self._cells[index[0]][index[1]].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            self._break_walls_r(index[0], index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column: cell._visited = False


    def solve(self): self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self._animate()
        if i == self._num_cols - 1 and j == self._num_rows - 1: return True
        cell = self._cells[i][j]
        cell._visited = True
        next_cells = []
        if not cell.has_left_wall: next_cells.append((i - 1, j))
        if not cell.has_bottom_wall: next_cells.append((i, j + 1))
        if not cell.has_right_wall: next_cells.append((i + 1, j))
        if not cell.has_top_wall and not (i == 0 and j == 0): next_cells.append((i, j - 1))
        not_visited = [index for index in next_cells if not self._cells[index[0]][index[1]]._visited]
        if not not_visited: return False
        for ij in not_visited: 
            cell.draw_move(self._cells[ij[0]][ij[1]])
            if self._solve_r(ij[0], ij[1]): return True
            self._cells[ij[0]][ij[1]].draw_move(cell, True)




