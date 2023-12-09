import sys
import re

data = sys.stdin.read().split("\n")
result = 0

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
regex = r"^one|two|three|four|five|six|seven|eight|nine|ten|[0-9]"

def match_to_num(match):
    if match in nums:
        return nums.index(match) + 1
    else:
        return int(match)

for line in data:
    matches = []
    for i in range(len(line)):
        matches.append(re.match(regex, line[i:]))
    matches = [match.group(0) for match in matches if match]
    contribution = int(match_to_num(matches[0])) * 10 + int(match_to_num(matches[-1]))
    print(f"{line} -> {matches} -> {contribution}")
    result += contribution

print(result)