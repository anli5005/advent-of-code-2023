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

result = 0

for str in strs:
    h = custom_hash(str)
    print(f"{str} -> {h}")
    result += h

print(result)
