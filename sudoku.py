# A Sudoku solver
import numpy as np

# input grid
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# function that checks if a cell can have a number 'n' as a solution
def possible(x, y, n):
    global grid
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == n:
                return False
    return True

# solver function using backtracking and recursion
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))

solve()
