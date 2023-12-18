import sys
import re

lines = sys.stdin.read().split("\n")

dig_plan = {}
grid = [[False for _ in range(1000)] for _ in range(1000)]
current = (0, 0)
dirs = {"0": (0, 1), "3": (-1, 0), "1": (1, 0), "2": (0, -1)}
imap = set([0])
jmap = set([0])

def parse_line(line: str):
    code = line.split(" ")[2]
    return int(code[2:7], 16), code[7]

for line in lines:
    amount, direction = parse_line(line)
    di, dj = dirs[direction]
    i = current[0] + di * amount
    j = current[1] + dj * amount
    current = (i, j)
    imap.add(i)
    imap.add(i + 0.5)
    jmap.add(j)
    jmap.add(j + 0.5)

imap = list(sorted(imap))
jmap = list(sorted(jmap))
imapr = {v: i for i, v in enumerate(imap)}
jmapr = {v: i for i, v in enumerate(jmap)}
current = (0, 0)

for line in lines:
    amount, direction = parse_line(line)
    di, dj = dirs[direction]
    target = (current[0] + di * amount, current[1] + dj * amount)
    gridi = imapr[current[0]]
    gridj = jmapr[current[1]]
    grid[gridi][gridj] = True
    while current != target:
        gridi += di
        gridj += dj
        current = (imap[gridi], jmap[gridj])
        grid[gridi][gridj] = True

print("\n".join("".join("#" if x else "." for x in row[:100]) + f" {i}" for i, row in enumerate(grid[:2])))

start = [(imapr[0] + 2, jmapr[0] + 2)]
while len(start) > 0:
    current = start.pop()
    i, j = current
    if grid[i][j]:
        continue
    grid[i][j] = True
    for _, v in dirs.items():
        try:
            if not grid[i + v[0]][j + v[1]]:
                start.append((i + v[0], j + v[1]))
        except:
            pass

result = 0

for i in range(0, len(imap), 2):
    idelta = imap[i + 2] - imap[i] if i + 2 < len(imap) else 1
    for j in range(0, len(jmap), 2):
        jdelta = jmap[j + 2] - jmap[j] if j + 2 < len(jmap) else 1
        if grid[i + 1][j + 1]:
            # print(f"grid[{i}][{j}] - {idelta - 1} * {jdelta - 1}")
            result += (idelta - 1) * (jdelta - 1)
        if grid[i][j + 1]:
            # print(f"grid[{i}][{j}] - {jdelta - 1}")
            result += jdelta - 1
        if grid[i + 1][j]:
            # print(f"grid[{i}][{j}] - {idelta - 1}")
            result += idelta - 1
        if grid[i][j]:
            # print(f"grid[{i}][{j}] - 1")
            result += 1

print(result)
