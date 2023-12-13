import sys
import re

patterns = sys.stdin.read().split("\n\n")

def analyze_reflections(rows: list[str]) -> int:
    possible = []
    for i in range(1, len(rows)):
        l = min(i, len(rows) - i)
        #for l in range(1, lm + 1):
        if rows[(i-l):i] == rows[i:i+l][::-1]:
            possible.append((i, 100))
    cols = [[] for _ in range(len(rows[0]))]
    for i in range(len(rows[0])):
        for j in range(len(rows)):
            cols[i].append(rows[j][i])
    for i in range(1, len(cols)):
        l = min(i, len(cols) - i)
        #for l in range(1, lm + 1):
        if cols[(i-l):i] == cols[i:i+l][::-1]:
            possible.append((i, 1))
    return possible

result = 0

for pattern in patterns:
    lines = pattern.split("\n")
    print(pattern)
    old_answers = set(analyze_reflections(lines))
    print(old_answers)
    stop = False
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            orig = lines[i]
            opp = "." if lines[i][j] == "#" else "#"
            l = list(lines[i])
            l[j] = opp
            lines[i] = "".join(l)
            possible_answers = set(analyze_reflections(lines))
            # print(possible_answers)
            if possible_answers - old_answers != set():
                possible_answer = list(possible_answers - old_answers)[0]
                print(possible_answers - old_answers)
                result += possible_answer[0] * possible_answer[1]
                stop = True
            lines[i] = orig
            if stop:
                break
        if stop:
            break
    if not stop:
        raise Exception("No answer found")

print(result)
