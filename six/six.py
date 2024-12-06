import numpy as np

moved_up = set()
moved_right = set()
moved_down = set()
moved_left = set()


def go_up(x, y, grid):
    # Loop
    if (x, y) in moved_up:
        return -2, -2
    moved_up.add((x, y))
    x -= 1
    while x > 0 and grid[x-1, y][0] != "#":
        if (x, y) in moved_up:
            return -2, -2
        grid[x, y] = "X"
        moved_up.add((x, y))
        x -= 1
    if (x, y) in moved_up:
        return -2, -2
    grid[x, y] = "X"
    moved_up.add((x, y))
    # Escaped upwards, done
    if x == 0:
        return -1, -1
    # Hit something
    if grid[x - 1, y] == "#":
        return x, y
    print(x, y)
    print(grid)
    raise ValueError()


def go_right(x, y, grid):
    # Loop
    if (x, y) in moved_right:
        return -2, -2
    moved_right.add((x, y))
    y += 1
    while y < len(grid[0]) - 1 and grid[x, y+1] != "#":
        if (x, y) in moved_right:
            return -2, -2
        grid[x, y] = "X"
        moved_right.add((x, y))
        y += 1
    if (x, y) in moved_right:
        return -2, -2
    grid[x, y] = "X"
    moved_right.add((x, y))
    # Escaped rightwards, done
    if y == len(grid[0]) - 1:
        return -1, -1
    # Hit something
    if grid[x, y+1] == "#":
        return x, y
    raise ValueError()


def go_down(x, y, grid):
    #Loop
    if (x, y) in moved_down:
        return -2, -2
    moved_down.add((x, y))
    x += 1
    while x < len(grid) - 1 and grid[x+1, y] != "#":
        if (x, y) in moved_down:
            return -2, -2
        grid[x, y] = "X"
        moved_down.add((x, y))
        x += 1
    if (x, y) in moved_down:
        return -2, -2
    grid[x, y] = "X"
    moved_down.add((x, y))
    # Escaped downwards, done
    if x == len(grid) - 1:
        return -1, -1
    # Hit something
    if grid[x+1, y] == "#":
        return x, y
    raise ValueError()


def go_left(x, y, grid):
    #Loop
    if (x, y) in moved_left:
        return -2, -2
    moved_left.add((x, y))
    y -= 1
    while y > 0 and grid[x, y-1] != "#":
        if (x, y) in moved_left:
            return -2, -2
        grid[x, y] = "X"
        moved_left.add((x, y))
        y -= 1
    if (x, y) in moved_left:
        return -2, -2
    grid[x, y] = "X"
    moved_left.add((x, y))
    # Escaped leftwards, done
    if y == 0:
        return -1, -1
    # Hit something
    if grid[x, y-1] == "#":
        return x, y
    raise ValueError()


f = open("test.txt")

og_grid = np.array([[x for x in line.strip('\n')] for line in f.readlines()])

start_x, start_y = np.where(og_grid == "^")
x = start_x[0]
y = start_y[0]
grid = og_grid.copy()
grid[x, y] = "X"
escaped = False
while not escaped:
    if x >= 0:
        x, y = go_up(x, y, grid)
    if x >= 0:
        x, y = go_right(x, y, grid)
    if x >= 0:
        x, y = go_down(x, y, grid)
    if x >= 0:
        x, y = go_left(x, y, grid)
    else:
        escaped = True
print(grid)

print("pt 1", np.count_nonzero(grid == "X"))

loop_spots = 0

i = 0
while i < len(og_grid):
    # print("i", i)
    j = 0
    while j < len(og_grid[0]):
        if i != start_x or j != start_y:
            grid = og_grid.copy()
            grid[i, j] = "#"
            escaped = False
            x = start_x[0]
            y = start_y[0]

            moved_up = set()
            moved_right = set()
            moved_down = set()
            moved_left = set()
            while not escaped:
                if x != -1 and x != -2:
                    x, y = go_up(x, y, grid)
                if x != -1 and x != -2:
                    x, y = go_right(x, y, grid)
                if x != -1 and x != -2:
                    x, y = go_down(x, y, grid)
                if x != -1 and x != -2:
                    x, y = go_left(x, y, grid)
                else:
                    escaped = True
                    if x == -2:
                        print("i,j", i, j)
                        loop_spots += 1
        j += 1
    i += 1

print("pt 2", loop_spots)
