import sys
import re

lines = sys.stdin.read().split("\n")
grid = []
for line in lines:
    grid.append(list(line))

while True:
    dirty = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                if i > 0 and grid[i - 1][j] == ".":
                    grid[i - 1][j] = "O"
                    grid[i][j] = "."
                    dirty = True
    if not dirty:
        break

result = 0

i = len(grid)
for row in grid:
    for cell in row:
        if cell == "O":
            result += i
    print("".join(row))
    i -= 1

print(result)
