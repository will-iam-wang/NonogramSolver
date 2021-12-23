from OneLineSolver import OneLineSolver
from PuzzleReader import PuzzleReader
from Cell import Cell

from copy import copy
import math
import time

class NonogramSolver:
    def __init__(self, puzzle_id):
        reader = PuzzleReader(puzzle_id)

        self.row_groups = reader.get_row_groups()
        self.col_groups = reader.get_col_groups()
        self.color_panel = reader.get_color_panel()

        self.color_cnt = len(self.color_panel)

        self.m = len(self.row_groups)
        self.n = len(self.col_groups)

        self.row_masks = [[(1 << self.color_cnt) - 1] * self.n for _ in range(self.m)]
        self.col_masks = [[(1 << self.color_cnt) - 1] * self.m for _ in range(self.n)]

        self.solver = OneLineSolver(max(self.n, self.m))

    def solve(self):
        dead_rows = [False] * self.m
        dead_cols = [False] * self.n
        ans = [[x[:] for x in self.row_masks]]
        
        start_time = time.time()

        prev_sum = -1
        while True:
            if not self.update_state(self.solver, dead_rows, dead_cols):
                print("Unable to update further")
                return []
            cur_sum = self.update_cell_values()
            if cur_sum == prev_sum:
                print("Solving progress completed")
                break
            prev_sum = cur_sum
            ans.append([x[:] for x in self.row_masks])
            
        print("--- %s seconds ---" % (time.time() - start_time))
        return ans

    def update_state(self, solver, dead_rows, dead_cols):
        row_masks = copy(self.row_masks)
        col_masks = copy(self.col_masks)
        row_groups = copy(self.row_groups)
        col_groups = copy(self.col_groups)

        if not self.update_groups_state(solver, dead_rows, row_groups, row_masks):
            return False
        if not self.update_groups_state(solver, dead_cols, col_groups, col_masks):
            return False
        return True

    @staticmethod
    def update_groups_state(solver, dead, groups, masks):
        for i in range(len(groups)):
            if not dead[i]:
                if not solver.update_state(groups[i], masks[i]):
                    return False
                is_dead = True
                for num in masks[i]:
                    if bin(num).count('1') != 1:
                        is_dead = False
                        break
                dead[i] = is_dead
        return True

    def update_cell_values(self):
        total = 0
        row_masks = copy(self.row_masks)
        col_masks = copy(self.col_masks)
        for row in range(self.m):
            for col in range(self.n):
                row_masks[row][col] &= col_masks[col][row]
                col_masks[col][row] &= row_masks[row][col]
                total += row_masks[row][col]
        return total
    

solver = NonogramSolver('36134')
solving_progress = solver.solve()
sss
m = len(solving_progress[0])
n = len(solving_progress[0][0])
w = 20
step = 0

grid = [[Cell(i, j, w) for i in range(n)] for j in range(m)]

def setup():
    size(n * w, m * w)
    
def draw():    
    background('#454545')
    for i in range(m):
        for j in range(n):
            x = solving_progress[step][i][j]
            c = 1
            if (x & (x - 1) == 0) and x != 0:
                c = int(math.log(x, 2)) + 1
            grid[i][j].update_color(solver.color_panel[c])
            grid[i][j].show()

def keyPressed():
    global step
    if key == 'w':
        step = min(step + 1, len(solving_progress) - 1)
    if key == 's':
        step = max(step - 1, 0)
