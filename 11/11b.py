import sys
import math
import re

lines = sys.stdin.read().split("\n")
big = 1000000

orig_grid = []
for line in lines:
    orig_grid.append(list(line))

num_galaxies = 0

grid = []
orig_cols = len(orig_grid[0])
for row in orig_grid:
    empty = ["."] * orig_cols
    if row == empty:
        grid.append(["!"] * orig_cols)
    new_row = []
    for ch in row:
        if ch != ".":
            new_row.append(num_galaxies)
            num_galaxies += 1
        else:
            new_row.append(ch)
    grid.append(new_row)

empty_columns = []
for i in range(orig_cols):
    empty = True
    for row in grid:
        if row[i] != "." and row[i] != "!":
            empty = False
    if empty:
        empty_columns.append(i)

orig_grid = grid
grid = [[] for row in orig_grid]
for col in range(orig_cols):
    for row in range(len(orig_grid)):
        grid[row].append(orig_grid[row][col])
    if col in empty_columns:
        for row in range(len(orig_grid)):
            grid[row].append("!")

result = 0

lookup_cache = {}
def lookup(grid, ch: int) -> (int, int):
    global lookup_cache
    if ch in lookup_cache:
        return lookup_cache[ch]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ch:
                lookup_cache[ch] = (row, col)
                return (row, col)
    return None

for row in grid:
    print(row)

pairs = 0
for i in range(num_galaxies):
    for j in range(i + 1, num_galaxies):
        # Figure out where i and j are
        i_pos = lookup(grid, i)
        j_pos = lookup(grid, j)
        dist = abs(i_pos[0] - j_pos[0]) + abs(i_pos[1] - j_pos[1])
        for row in range(min(i_pos[0], j_pos[0]), max(i_pos[0], j_pos[0]) + 1):
            if grid[row][0] == "!":
                dist += big - 2
        for col in range(min(i_pos[1], j_pos[1]), max(i_pos[1], j_pos[1]) + 1):
            if grid[0][col] == "!":
                dist += big - 2
        # print(f"{i} and {j} are {dist} apart")
        result += dist
        pairs += 1
        if pairs % 10000 == 0:
            print(f"Pairs: {pairs}")

print(result)
