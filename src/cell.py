from graphics import Point, Line


class Cell():
    def __init__(self, window=None):
        self.has_left_wall, self.has_right_wall = True, True
        self.has_top_wall, self.has_bottom_wall = True, True
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self._win = window
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        if not self._win: return
        color = lambda x: "black" if x else "white"
        self._x1, self._x2, self._y1, self._y2 = x1, x2, y1, y2
        top_left, top_right = Point(x1, y1), Point(x2, y1)
        bottom_left, bottom_right = Point(x1, y2), Point(x2, y2)
        self._win.draw_line(Line(top_left, top_right), color(self.has_top_wall))
        self._win.draw_line(Line(bottom_left, bottom_right), color(self.has_bottom_wall))
        self._win.draw_line(Line(top_right, bottom_right), color(self.has_right_wall))
        self._win.draw_line(Line(top_left, bottom_left), color(self.has_left_wall))

    def draw_move(self, to_cell, undo=False):
        if not self._win: return
        if undo: color = "red"
        else: color = "gray"
        _from = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(_from, to), color)

    def visit(self): self._visited = True

