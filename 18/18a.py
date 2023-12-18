import sys
import re

lines = sys.stdin.read().split("\n")

dig_plan = {}
grid = [[False for _ in range(1000)] for _ in range(1000)]
grid[0][0] = True
current = (0, 0)
dirs = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}

for line in lines:
    parts = line.split(" ")
    direction = parts[0]
    amount = int(parts[1])
    di, dj = dirs[direction]
    for l in range(amount):
        i = current[0] + di
        j = current[1] + dj
        current = (i, j)
        grid[i][j] = True

start = [(1, 1)]
seen = set()
while len(start) > 0:
    current = start.pop()
    if current in seen:
        continue
    seen.add(current)
    i, j = current
    grid[i][j] = True
    for _, v in dirs.items():
        if not grid[i + v[0]][j + v[1]]:
            start.append((i + v[0], j + v[1]))

result = sum(sum(1 for x in row if x) for row in grid)

print(result)
