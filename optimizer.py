import SudikuGrid
import MainSolver


def fillsinglespace():
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(1, 10):
                if MainSolver.check(i, j, k) == 1:
                    count = count + 1
            if count == 1:
                for l in range(1, 10):
                    if MainSolver.check(i, j, k) == 1:
                        SudikuGrid.sudoku_grid[i][j] = l
                        break
            else:
                continue
