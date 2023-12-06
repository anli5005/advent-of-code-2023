import sys
import re

lines = sys.stdin.read().split("\n")
races = []

time_str = lines[0].split()[1:]
dist_str = lines[1].split()[1:]

races = [(int("".join(time_str)), int("".join(dist_str)))]

print(races)
result = 1
for time, dist in races:
    wins = 0
    for i in range(time):
        speed = i
        distance = (time - i) * speed
        if distance > dist:
            wins += 1
    result *= wins

print(result)