import sys

data = sys.stdin.read().split("\n")
result = 0

for line in data:
    digits = list(filter(lambda x: x.isdigit(), line))
    contribution = int(digits[0]) * 10 + int(digits[-1])
    result += contribution

print(result)