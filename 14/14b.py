import sys
import re

lines = sys.stdin.read().split("\n")
grid = []
for line in lines:
    grid.append(list(line))

def tilt_board(get_pos):
    while True:
        dirty = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "O":
                    new_i, new_j = get_pos(i, j)
                    if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[i]):
                        if grid[new_i][new_j] == ".":
                            grid[new_i][new_j] = "O"
                            grid[i][j] = "."
                            dirty = True
        if not dirty:
            break

last_boards = []
i = 0
max_it = 1e9
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while i < max_it:
    if len(last_boards) > 100:
        last_boards.pop(0)
    last_boards.append([row[:] for row in grid])
    tilt_board(lambda i, j: (i - 1, j))
    tilt_board(lambda i, j: (i, j - 1))
    tilt_board(lambda i, j: (i + 1, j))
    tilt_board(lambda i, j: (i, j + 1))
    if grid in last_boards:
        index = last_boards.index(grid)
        distance = len(last_boards) - index
        print(f"Grid in last_boards at iteration {i}, index {index}!")
        i += ((max_it - i) // distance) * distance + 1
        print(f"Skipped to {i}")
        last_boards = []
    else:
        i += 1
    if i % 100000 == 0:
        print(f"i = {i}")

result = 0

i = len(grid)
for row in grid:
    for cell in row:
        if cell == "O":
            result += i
    print("".join(row))
    i -= 1

print(result)
