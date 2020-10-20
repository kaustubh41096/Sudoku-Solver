import SudikuGrid


def fillsinglespace():
    numbers = 0
    for i in range(0, 9):
        for j in range(0, 9):
            count = 0
            for k in range(1, 10):
                if check(i, j, k) == 1:
                    count = count + 1
            if count == 1:
                for l in range(1, 10):
                    if check(i, j, k) == 1:
                        SudikuGrid.sudoku_grid[i][j] = l
                        numbers = numbers + 1
                        break
            else:
                continue


def grid_full():
    for i in range(0, 9):
        for j in range(0, 9):
            if SudikuGrid.sudoku_grid[i][j] != 0:
                return 0
    if i and j == 8:
        return 1


def check_row(num, pos):
    i = 0
    while i < 9:
        if SudikuGrid.sudoku_grid[pos][i] != num:
            i = i + 1
        else:
            return 0
    if i == 9:
        return 1


def check_column(num, pos):
    i = 0
    while i < 9:
        if SudikuGrid.sudoku_grid[i][pos] != num:
            i = i + 1
        else:
            return 0
    if i == 9:
        return 1


def check_box(num, posx, posy):
    if posx < 3 and posy < 3:
        # box = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 2 and j == 2:
            # print(i, j)
            return 1
    elif posx < 3 and 2 < posy < 6:
        # box = 2
        for i in range(0, 3):
            for j in range(3, 6):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    # print(0)
                    return 0
        if i == 2 and j == 5:
            return 1
    elif posx < 3 and 5 < posy < 9:
        # box = 3
        for i in range(0, 3):
            for j in range(6, 9):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 2 and j == 8:
            return 1
    elif 2 < posx < 6 and posy < 3:
        # box = 4
        for i in range(3, 6):
            for j in range(0, 3):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 5 and j == 2:
            return 1
    elif 2 < posx < 6 and 2 < posy < 6:
        # box = 5
        for i in range(3, 6):
            for j in range(3, 6):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 5 and j == 5:
            return 1
    elif 2 < posx < 6 and 5 < posy < 9:
        # box = 6
        for i in range(3, 6):
            for j in range(6, 9):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 5 and j == 8:
            return 1
    elif 5 < posx < 9 and posy < 3:
        # box = 7
        for i in range(6, 9):
            for j in range(0, 3):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 8 and j == 2:
            return 1
    elif 5 < posx < 9 and 2 < posy < 6:
        # box = 8
        for i in range(6, 9):
            for j in range(3, 6):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 8 and j == 5:
            return 1
    elif 5 < posx < 9 and 5 < posy < 9:
        # box = 9
        for i in range(6, 9):
            for j in range(6, 9):
                if num == SudikuGrid.sudoku_grid[i][j]:
                    return 0
        if i == 8 and j == 8:
            return 1


def check(posx, posy, num):
    print(posx, posy, num)
    print(check_row(num, posx), check_column(num, posy), check_box(num, posx, posy))
    if SudikuGrid.sudokugrid_copy[posx][posy] == 0:
        if (check_row(num, posx) and check_box(num, posx, posy)) and check_column(num, posy) == 1:
            return 1
        else:
            return 0
    else:
        # print(check_row(num, posx), check_column(num, posy), check_box(num, posx, posy))
        return 2


def print_grid():
    for i in range(0, 9):
        for j in range(0, 9):
            if j in [2, 5]:
                print(str(SudikuGrid.sudoku_grid[i][j]) + "|", end='')
            else:
                print(SudikuGrid.sudoku_grid[i][j], end='')
        if i in [2, 5]:
            print("\n-----------")
        else:
            print()
    print("-----------------------------")


def insert_num(posx, posy):
    posx1 = posx
    posy1 = posy
    # print(posx1, posy1)
    while grid_full() == 0:
        fillsinglespace()
        while posx1 < 9:
            while posy1 < 9:
                for num in range(1, 10):
                    if check(posx1, posy1, num) == 1 and check(posx1, posy1, num) != 2:
                        SudikuGrid.sudoku_grid[posx1][posy1] = num
                        print_grid()
                        insert_num(posx1, posy1 + 1)
                    elif check(posx1, posy1, num) == 2:
                        insert_num(posx1, posy1 + 1)
                        return
                    else:
                        continue
                if num == 9:
                    SudikuGrid.sudoku_grid[posx1][posy1] = 0
                    return
            if posy1 == 9:
                posx1 = posx1 + 1
                posy1 = 0


print_grid()
insert_num(0, 0)

