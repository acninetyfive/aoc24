import numpy as np

mas = ['M', 'A', 'S']


def check_left(x, y):
    if y >= 3:
        if np.array_equal(grid[x, y-3:y][::-1], mas):
            return True
    return False


def check_right(x, y):
    if y < len(grid[0]) - 3:
        if np.array_equal(grid[x, y+1:y+4], mas):
            return True
    return False


def check_up(x, y):
    if x >= 3:
        if np.array_equal(grid[x-3:x, y][::-1], mas):
            return True


def check_down(x, y):
    if x < len(grid) - 3:
        if np.array_equal(grid[x+1:x+4, y], mas):
            return True
    return False


def check_up_left(x, y):
    if x >= 3 and y >= 3:
        if np.array_equal([grid[x-i, y-i] for i in range(1, 4)], mas):
            return True
    return False


def check_up_right(x, y):
    if x >= 3 and y < len(grid[0]) - 3:
        if np.array_equal([grid[x-i, y+i] for i in range(1, 4)], mas):
            return True
    return False


def check_down_left(x, y):
    if x < len(grid) - 3 and y >= 3:
        if np.array_equal([grid[x+i, y-i] for i in range(1, 4)], mas):
            return True
    return False


def check_down_right(x, y):
    if x < len(grid) - 3 and y < len(grid[0]) - 3:
        if np.array_equal([grid[x+i, y+i] for i in range(1, 4)], mas):
            return True
    return False


def check_all_directions(x, y):
    count = 0
    if check_left(x, y):
        count += 1
    if check_right(x, y):
        count += 1
    if check_up(x, y):
        count += 1
    if check_down(x, y):
        count += 1
    if check_up_left(x, y):
        count += 1
    if check_up_right(x, y):
        count += 1
    if check_down_left(x, y):
        count += 1
    if check_down_right(x, y):
        count += 1
    return count


def check_back_diag(x, y):
    if (grid[x-1, y-1] == 'M' and 
        grid[x+1, y+1] == 'S') or (
            grid[x-1, y-1] == 'S' and 
            grid[x+1, y+1] == 'M'
        ):
        return True
    return False


def check_front_diag(x, y):
    if (grid[x-1, y+1] == 'M' and 
        grid[x+1, y-1] == 'S') or (
            grid[x-1, y+1] == 'S' and 
            grid[x+1, y-1] == 'M'
        ):
        return True
    return False


def check_x_mas(x, y):
    if x > 0 and x < len(grid) - 1 and y > 0 and y < len(grid[0]) - 1:
        if check_back_diag(x, y) and check_front_diag(x, y):
            return True
    return False


f = open("in.txt")

grid = np.array([[c for c in line[:-1]] for line in f.readlines()])

xmas_count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i, j] == 'X':
            xmas_count += check_all_directions(i, j)

print("pt 1", xmas_count)

x_mas_count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i, j] == 'A':
            x_mas_count += int(check_x_mas(i, j))

print("pt 2", x_mas_count)
