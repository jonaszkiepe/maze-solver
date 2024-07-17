from graphics import Window
import sys
from maze import Maze

sys.setrecursionlimit(3000)
def main():
   win = Window(1900, 1000) 
   num_cols = 70
   num_rows = 30
   m1 = Maze(30, 30, num_rows, num_cols, 20, 20, win, 0)
   m1.solve()
   win.wait_for_close()


if __name__ == "__main__": main()
