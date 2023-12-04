import sys
import re

lines = sys.stdin.read().split("\n")

result = 0

for line in lines:
    parts = line.split(": ")
    parts2 = parts[1].split(" | ")
    winning = parts2[0].split(" ")
    yours = parts2[1].split(" ")
    score = 0
    seen = set()
    for x in yours:
        if x in winning and x != "":
            seen.add(x)
            if score == 0:
                score = 1
            else:
                score *= 2
    result += score
    print(score)

print(result)