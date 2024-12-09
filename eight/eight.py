import numpy as np
from fractions import Fraction

chars = {'Q', 'O', 'z', 'J', '8', 'm', 'k', 'R', 'P', 'h', 'a', '9', '1', 
           'M', '2', '3', 'U', '4', '5', 'q', 'f', 'p', '6', 'K', 'D', 'F',
           'u', '7', 'N', 'L', 'X', 'A', 'j', 'B', 'v', 'H', 'r', 'd', 'l',
           'o', 'Z', 'x', 'i', 'I', 'b', 'n', 'V', '0'}

f = open("t.txt")

grid = np.array([[c for c in line.strip('\n')] for line in f.readlines()])


def get_line_equation(point1, point2):
    """Gets the equation of a line from two points.

    Args:
        point1 (tuple): The first point (x1, y1).
        point2 (tuple): The second point (x2, y2).

    Returns:
        tuple: The slope (m) and y-intercept (b) of the line.
    """

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the slope
    m = (x2 - x1) / (y2 - y1) if y1 != y2 else float('inf')
    if m == float('inf'):
        return m, y1
    # Calculate the y-intercept
    b = x1 - m * y1

    return m, b


def get_lattice(m, b):
    s = set()
    if m == float('inf'):
        for x in range(0, len(grid)):
            s.add((x, b))
    else:
        for x in range(len(grid)):
            for y in range(len(grid)):
                a_y = y
                a_x = m * y + b
                if a_x >= 0 and a_x < len(grid):
                    if a_y >= 0 and a_y < len(grid[0]):
                        if a_x == int(a_x) and a_y == int(a_y):
                            s.add((int(a_x), int(a_y)))
    return s


def find_antinodes(a, b):
    s = set()
    x_dist = abs(a[0] - b[0])
    y_dist = abs(a[1] - b[1])

    # a is above or in line with b
    if a[0] <= b[0]:
        a_x = a[0] - x_dist
        b_x = b[0] + x_dist
    else:
        a_x = a[0] + x_dist
        b_x = b[0] - x_dist
    
    # a is left of or in line with b
    if a[1] <= b[1]:
        a_y = a[1] - y_dist
        b_y = b[1] + y_dist
    else:
        a_y = a[1] + y_dist
        b_y = b[1] - y_dist

    if a_x >= 0 and a_x < len(grid):
        if a_y >= 0 and a_y < len(grid[0]):
            s.add((a_x, a_y))
    if b_x >= 0 and b_x < len(grid):
        if b_y >= 0 and b_y < len(grid[0]):
            s.add((b_x, b_y))
    
    return s


antinodes = set()

for c in chars:
    w = np.where(grid == c)
    if len(w[0]) > 1:
        #print(c, w)
        for i in range(len(w[0]) - 1):
            for j in range(i+1, len(w[0])):
                if w[0][i] < w[0][j]:
                    first = (w[0][i], w[1][i])
                    second = (w[0][j], w[1][j])
                elif w[0][i] > w[0][j]:
                    second = (w[0][i], w[1][i])
                    first = (w[0][j], w[1][j])
                elif w[1][i] < w[1][j]:
                    first = (w[0][i], w[1][i])
                    second = (w[0][j], w[1][j])
                elif w[1][i] > w[1][j]:
                    second = (w[0][i], w[1][i])
                    first = (w[0][j], w[1][j])
                else:  # same number twice
                    raise ValueError()
                # a_nodes = find_antinodes(first, second)
                # if len(a_nodes) > 0:
                    # antinodes.update(a_nodes)
                m, b = get_line_equation(first, second)
                #print("m,b", m, b)
                a_nodes = get_lattice(m, b)
                if len(a_nodes) > 0:
                    antinodes.update(a_nodes)
a_l = list(antinodes)
a_l.sort(key=lambda x: (x[0], x[1]))
for a in a_l:
    print(a[0], a[1])
print("count = ", len(antinodes))
