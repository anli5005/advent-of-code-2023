import sys
import re

lines = sys.stdin.read().split("\n")

copies = [1 for _ in range(len(lines))]
#copies[0] = 1

i = 0
for line in lines:
    parts = line.split(": ")
    parts2 = parts[1].split(" | ")
    winning = parts2[0].split(" ")
    yours = parts2[1].split(" ")
    score = 0
    for x in yours:
        if x in winning and x != "":
            score += 1
    for j in range(score):
        copies[i + j + 1] += copies[i]
    i += 1

print(copies)

print(sum(copies))