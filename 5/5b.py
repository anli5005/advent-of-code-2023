import sys
import re
from typing import Tuple

lines = sys.stdin.read().split("\n")

def ranges_intersect(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int] | None:
    if not (a[0] <= b[0] < (a[0] + a[1]) or b[0] <= a[0] < (b[0] + b[1])):
        return None

    if a[0] <= b[0] < (a[0] + a[1]):
        return b[0], min(a[0] + a[1] - b[0], b[1])
    else:
        return a[0], min(b[0] + b[1] - a[0], a[1])

initial_seeds_raw = [int(x) for x in lines[0].split(" ")[1:]]
seeds = []
for i in range(0, len(initial_seeds_raw), 2):
    seeds.append((initial_seeds_raw[i], initial_seeds_raw[i+1]))

soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []

i = 1

def process_ranges(prev, next):
    global i
    temp_ranges = []

    for line in lines[i:]:
        if len(line) == 0:
            i += 1
            break
        dest, source, l = [int(x) for x in line.split(" ")]
        temp_ranges.append((source, l, dest))
        i += 1
    
    for prev_range in prev:
        intersected = []
        for next_range in temp_ranges:
            intersect = ranges_intersect((prev_range[0], prev_range[1]), (next_range[0], next_range[1]))
            if intersect is not None:
                intersected.append(intersect)
                next.append((intersect[0] - next_range[0] + next_range[2], intersect[1]))
        intersected.sort(key=lambda x: x[0])
        current_index = prev_range[0]
        for r in intersected:
            if r[0] > current_index:
                next.append((current_index, r[0] - current_index))
            current_index = r[0] + r[1]
        if current_index < prev_range[0] + prev_range[1]:
            next.append((current_index, prev_range[0] + prev_range[1] - current_index))
    
    print(f"{prev} -> {next}")

for line in lines[i:]:
    if line == "seed-to-soil map:":
        i += 1
        break
    i += 1

process_ranges(seeds, soil)

for line in lines[i:]:
    if line == "soil-to-fertilizer map:":
        i += 1
        break
    i += 1

process_ranges(soil, fertilizer)

for line in lines[i:]:
    if line == "fertilizer-to-water map:":
        i += 1
        break
    i += 1

process_ranges(fertilizer, water)

for line in lines[i:]:
    if line == "water-to-light map:":
        i += 1
        break
    i += 1

process_ranges(water, light)

for line in lines[i:]:
    if line == "light-to-temperature map:":
        i += 1
        break
    i += 1

process_ranges(light, temperature)

for line in lines[i:]:
    if line == "temperature-to-humidity map:":
        i += 1
        break
    i += 1

process_ranges(temperature, humidity)

for line in lines[i:]:
    if line == "humidity-to-location map:":
        i += 1
        break
    i += 1

process_ranges(humidity, location)

print(location)

print(min(loc[0] for loc in location))