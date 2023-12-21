import sys
import re

lines = sys.stdin.read().split("\n")
grid = [list(line) for line in lines]
queue = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            queue.add((i, j))

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for n in range(64):
    next_queue = set()
    for i, j in queue:
        for d in dirs:
            ni = i + d[0]
            nj = j + d[1]
            if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]) and grid[ni][nj] != "#":
                next_queue.add((ni, nj))
    queue = next_queue

for i, row in enumerate(grid):
    s = ""
    for j, c in enumerate(row):
        if (i, j) in queue:
            s += "O"
        else:
            s += c
    print(s)


result = len(queue)
print(result)
