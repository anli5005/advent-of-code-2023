# Note: This solution is incomplete

import sys
import re

lines = sys.stdin.read().split("\n")
grid = []
start_pos = None
s_ch = "F"

i = 0
for line in lines:
    grid.append(list(line))
    if "S" in line:
        start_pos = (i, line.index("S"))
    i += 1

def has_connection(r: int, c: int, direction: str) -> bool:
    pipe = grid[r][c]
    if direction == "north":
        return pipe in "S|LJ"
    elif direction == "east":
        return pipe in "S-LF"
    elif direction == "west":
        return pipe in "S-J7"
    elif direction == "south":
        return pipe in "S|F7"

def get_neighbors(r: int, c: int):
    neighbors = []
    if r > 0 and has_connection(r, c, "north"):
        if has_connection(r - 1, c, "south"):
            neighbors.append((r - 1, c))
    if c < len(grid[0]) - 1 and has_connection(r, c, "east"):
        if has_connection(r, c + 1, "west"):
            neighbors.append((r, c + 1))
    if c > 0 and has_connection(r, c, "west"):
        if has_connection(r, c - 1, "east"):
            neighbors.append((r, c - 1))
    if r < len(grid) - 1 and has_connection(r, c, "south"):
        if has_connection(r + 1, c, "north"):
            neighbors.append((r + 1, c))
    return neighbors

queue = [(start_pos, 0)]
in_loop = set()
while len(queue) > 0:
    pos, i = queue.pop(0)
    r, c = pos
    if (r, c) in in_loop:
        continue
    in_loop.add((r, c))
    for neighbor in get_neighbors(r, c):
        queue.append((neighbor, i + 1))

queue = []
for r, c in in_loop:
    new_r = r * 3 + 2
    new_c = c * 3 + 2
    g = grid[r][c]
    if grid[r][c] == "S":
        g = s_ch
    if g == "7":
        queue.append((new_r + 1, new_c - 1))
    elif g == "J":
        queue.append((new_r - 1, new_c - 1))
    elif g == "F":
        queue.append((new_r + 1, new_c + 1))
    elif g == "L":
        queue.append((new_r - 1, new_c + 1))

orig_rows = len(lines)
orig_cols = len(lines[0])

grid = []

i = 0
for line in lines:
    top = "."
    mid = "."
    bot = "."
    for ch in line:
        if ch == "S":
            ch = s_ch
        if ch == ".":
            top += "..."
            mid += "..."
            bot += "..."
        elif ch == "S":
            top += ".|."
            mid += "-S-"
            bot += ".|."
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
    top += "."
    mid += "."
    bot += "."
    grid.append(list(top))
    grid.append(list(mid))
    grid.append(list(bot))
    i += 1

grid.insert(0, ["."] * len(grid[0]))
grid.append(["."] * len(grid[0]))

result = 0

for l in grid:
    print("".join(l))

print(queue)

queue = [(q, set([q]), False) for q in queue]
visited = set()
outside = set()
while len(queue) > 0:
    pos, curr_set, add = queue.pop(0)
    new_set = set(curr_set)
    new_set.add(pos)
    r, c = pos
    if (r, c) in visited:
        continue
    visited.add((r, c))
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num_neighbors = 0
    for dr, dc in d:
        neighbor = (r + dr, c + dc)
        if neighbor[0] >= 0 and neighbor[0] <= len(grid) - 1 and neighbor[1] >= 0 and neighbor[1] <= len(grid[0]) - 1:
            if grid[neighbor[0]][neighbor[1]] == "." and neighbor not in visited:
                queue.append((neighbor, new_set, (r, c) in outside))
                num_neighbors += 1
                # print(neighbor)
    # print(f"({r}, {c}) -> {grid[r][c]}: {num_neighbors}")
    if num_neighbors == 0:
        # Are we in a space occupied by a loop?
        old_r = (r - 1) // 3
        old_c = (c - 1) // 3
        if (old_r, old_c) not in in_loop:
            for npos in new_set:
                if npos not in outside:
                    outside.add(npos)
                    queue.append((npos, set([npos]), True))
                    visited.remove(npos)
            # print(old_r, old_c)

for i in range(orig_rows):
    for j in range(orig_cols):
        coords = (i * 3 + 2, j * 3 + 2)
        if coords in visited and coords not in outside:
            print(coords)
            result += 1

print(result)
