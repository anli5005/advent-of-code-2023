import sys
import re

strs = sys.stdin.read().split(",")

def custom_hash(str):
    current = 0
    for c in str:
        current += ord(c)
        current *= 17
        current %= 256
    return current

boxes = [[] for _ in range(256)]
lengths = {}
result = 0

for str in strs:
    if "=" in str:
        label = str.split("=")[0]
        length = int(str.split("=")[1])
        h = custom_hash(label)
        if label not in boxes[h]:
            boxes[h].append(label)
        lengths[label] = length
    elif "-" in str:
        label = str.split("-")[0]
        h = custom_hash(label)
        if label in boxes[h]:
            boxes[h].remove(label)

for bi, box in enumerate(boxes):
    for li, label in enumerate(box):
        power = (bi + 1) * (li + 1) * lengths[label]
        print(f"{label} -> {power}")
        result += power

print(result)
