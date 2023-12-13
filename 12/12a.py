import sys
from collections import Counter

lines = sys.stdin.read().split("\n")

def build_candidates(line: str, out: list[str]) -> str:
    if "?" not in line:
        out.append(line)
        return
    i = line.index("?")
    build_candidates(line[:i] + "." + line[i+1:], out)
    build_candidates(line[:i] + "#" + line[i+1:], out)

result = 0

for line in lines:
    parts = line.split()

    expected = [int(x) for x in parts[1].split(",")]
    
    candidates = []
    build_candidates(parts[0], candidates)

    contribution = 0
    for candidate in candidates:
        current_dots = 0
        amounts = []
        for ch in candidate:
            if ch == "#":
                current_dots += 1
            elif current_dots != 0:
                amounts.append(current_dots)
                current_dots = 0
        if current_dots > 0:
            amounts.append(current_dots)
        if amounts == expected:
            contribution += 1
    result += contribution
    print(f"{line}: {contribution}")

print(result)
