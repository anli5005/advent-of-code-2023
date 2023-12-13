import sys
import re

patterns = sys.stdin.read().split("\n\n")

def analyze_reflections(rows: list[str]) -> int:
    for i in range(1, len(rows)):
        l = min(i, len(rows) - i)
        if rows[(i-l):i] == rows[i:i+l][::-1]:
            return i * 100
    cols = [[] for _ in range(len(rows[0]))]
    for i in range(len(rows[0])):
        for j in range(len(rows)):
            cols[i].append(rows[j][i])
    for i in range(1, len(cols)):
        l = min(i, len(cols) - i)
        if cols[(i-l):i] == cols[i:i+l][::-1]:
            return i

result = 0

for pattern in patterns:
    lines = pattern.split("\n")
    print(pattern)
    answer = analyze_reflections(lines)
    print(answer)
    result += answer

print(result)
