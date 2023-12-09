# Was looking up what people thought about Day 8 Part 2 when I chanced
# upon this:
# 
# https://www.reddit.com/r/adventofcode/comments/18dg1hw/2023_day_8_part_2_about_the_correctness_of_a/
# 
# I'm not the biggest fan of the solution; it requires making a major
# assumption about the problem input, and I wish it was explicitly
# documented in the problem statement. But it worked, and that's good
# enough, I guess?
# 
# (If someone has a general solution that runs faster than brute force,
# I'd love to see it.)

import sys
import re
import math

lines = sys.stdin.read().split("\n")

tree = {}
for line in lines[2:]:
    node, children_str = line.split(" = ")
    children = children_str[1:-1].split(", ")
    tree[node] = children

steps = lines[0]
paths = []

def get_path(node):
    i = 0
    current = node
    while True:
        step = steps[i % len(steps)]
        if step == "L":
            current = tree[current][0]
        else:
            current = tree[current][1]
        i += 1
        if current.endswith("Z"):
            return i

for node in tree:
    if node.endswith("A"):
        l = get_path(node)
        paths.append(l)
        print(f"Path from {node} is {l} steps long (remainder {l % len(steps)})")

result = math.lcm(*paths)
print(result)