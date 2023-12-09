import sys
import re

lines = sys.stdin.read().split("\n")

i = 1
result = 0
for line in lines:
    p = line.split(": ")
    i = int(p[0][len("Game "):])
    rounds = p[1].split("; ")
    r = 0
    g = 0
    b = 0
    for round in rounds:
        parts = round.split(", ")
        for part in parts:
            els = part.split(" ")
            if els[1] == "red":
                r = max(r, int(els[0]))
            elif els[1] == "green":
                g = max(g, int(els[0]))
            elif els[1] == "blue":
                b = max(b, int(els[0]))
    if r <= 12 and g <= 13 and b <= 14:
        result += i
        print(f"Game {i} possible")
    i += 1

print(result)