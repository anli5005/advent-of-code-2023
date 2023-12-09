import sys
import re

lines = sys.stdin.read().split("\n")

tree = {}
for line in lines[2:]:
    node, children_str = line.split(" = ")
    children = children_str[1:-1].split(", ")
    tree[node] = children

result = 0
print(tree)

steps = lines[0]
i = 0
current = "AAA"
while True:
    step = steps[i % len(steps)]
    if step == "L":
        current = tree[current][0]
    else:
        current = tree[current][1]
    i += 1
    if current == "ZZZ":
        result = i
        break

print(result)
