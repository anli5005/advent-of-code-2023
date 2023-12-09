import sys
import re

lines = sys.stdin.read().split("\n")

result = 0

for line in lines:
    nums = [int(x) for x in line.split()]
    diff = [nums]
    while len(diff[-1]) > 0:
        last = diff[-1]
        diff.append([last[i + 1] - last[i] for i in range(len(last) - 1)])
    diff[-1].insert(0, 0)
    for i in range(len(diff) - 2, -1, -1):
        diff[i].insert(0, diff[i][0] - diff[i + 1][0])
    print(diff)
    result += diff[0][0]

print(result)
