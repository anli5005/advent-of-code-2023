import sys
import re

lines = sys.stdin.read().split("\n")
already_considered = set()

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

i = 0
result = 0
matrix = []
for line in lines:
    matrix.append(line)

for i in range(len(lines)):
    j = 0
    for ch in matrix[i]:
        if ch == "*":
            ratio = 1
            gears = 0
            should_add = set()
            for di, dj in d:
                if 0 <= i + di < len(matrix) and 0 <= j + dj < len(matrix[0]):
                    # Go leftwards until we find a non-digit character or beginning of string
                    line = matrix[i + di]
                    k = j + dj
                    while k >= 0 and line[k].isdigit():
                        k -= 1
                    k += 1
                    # Go rightwards until we find a non-digit character or end of string
                    l = j + dj
                    while l < len(line) and line[l].isdigit():
                        l += 1
                    l -= 1
                    # print(f"{ch}, {di}, {dj} -> {k}, {l}")
                    if k > l:
                        # print("Skip")
                        continue
                    should_add = True
                    for m in range(k, l + 1):
                        if (i + di, m) in already_considered:
                            should_add = False
                        else:
                            already_considered.add((i + di, m))
                    if should_add:
                        gears += 1
                        num = int(line[k:l + 1])
                        ratio *= num
                        print(f"Adding {num} - closest to {ch}")
            if gears == 2:
                result += ratio
        j += 1
    i += 1

print(result)