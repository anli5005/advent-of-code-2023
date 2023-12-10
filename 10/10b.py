# Naive BFS-based solution
# Pretty slow lol

import sys
import re

lines = sys.stdin.read().split("\n")
orig_rows = len(lines)
orig_cols = len(lines[0])

grid = []
start_pos = None

i = 0
for line in lines:
    top = "#"
    mid = "#"
    bot = "#"
    for ch in line:
        if ch == "S":
            top += "..."
            mid += ".S."
            bot += "..."
        elif ch == ".":
            top += "..."
            mid += "..."
            bot += "..."
        elif ch == "L":
            top += ".|."
            mid += ".L-"
            bot += "..."
        elif ch == "J":
            top += ".|."
            mid += "-J."
            bot += "..."
        elif ch == "F":
            top += "..."
            mid += ".F-"
            bot += ".|."
        elif ch == "7":
            top += "..."
            mid += "-7."
            bot += ".|."
        elif ch == "-":
            top += "..."
            mid += "---"
            bot += "..."
        elif ch == "|":
            top += ".|."
            mid += ".|."
            bot += ".|."
    top += "#"
    mid += "#"
    bot += "#"
    grid.append(list(top))
    grid.append(list(mid))
    grid.append(list(bot))
    i += 1

grid.insert(0, ["#"] * len(grid[0]))
grid.append(["#"] * len(grid[0]))

for i in range(len(grid)):
    row = ""
    for j in range(len(grid[i])):
        row += grid[i][j]
    print(row)

def fill_s():
    global start_pos
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start_pos = (i, j)
                d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in d:
                    try:
                        if grid[i + dr * 2][j + dc * 2] != "." and grid[i + dr * 2][j + dc * 2] != "#":
                            grid[i + dr][j + dc] = "S"
                    except:
                        pass
                return

fill_s()

queue = [start_pos]
in_loop = set()
while len(queue) > 0:
    pos = queue.pop(0)
    r, c = pos
    if (r, c) in in_loop:
        continue
    in_loop.add((r, c))
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in d:
        neighbor = (r + dr, c + dc)
        if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0]):
            if grid[neighbor[0]][neighbor[1]] != ".":
                queue.append(neighbor)

def run_bfs(r: int, c: int):
    queue = [(r, c)]
    visited = set()
    pipes = set()
    while len(queue) > 0:
        pos = queue.pop(0)
        r, c = pos
        if (r, c) in visited:
            continue
        visited.add((r, c))
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in d:
            neighbor = (r + dr, c + dc)
            if neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == "#":
                    return set("bad")
                if neighbor not in in_loop:
                    queue.append(neighbor)
    return pipes

result = 0
answers = []

for i in range(orig_rows):
    for j in range(orig_cols):
        coords = (i * 3 + 2, j * 3 + 2)
        if coords in in_loop:
            continue
        pipes = run_bfs(coords[0], coords[1])
        if pipes - in_loop == set():
            answers.append(coords)
            result += 1
    print(f"{i + 1}/{orig_rows}")

for i in range(len(grid)):
    row = ""
    for j in range(len(grid[i])):
        if (i, j) in answers:
            row += "@"
        elif (i, j) in in_loop:
            row += "X"
        else:
            row += grid[i][j]
    print(row)

print(result)
