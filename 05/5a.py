import sys
import re

lines = sys.stdin.read().split("\n")

seeds = {}
soil = {}
fertilizer = {}
water = {}
light = {}
temperature = {}
humidity = {}
location = {}

initial_seeds = [int(x) for x in lines[0].split(" ")[1:]]

i = 1
for line in lines[i:]:
    if line == "seed-to-soil map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = seeds
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

#print(line)

for line in lines[i:]:
    if line == "soil-to-fertilizer map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = soil
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

for line in lines[i:]:
    if line == "fertilizer-to-water map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = fertilizer
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

for line in lines[i:]:
    if line == "water-to-light map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = water
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

for line in lines[i:]:
    if line == "light-to-temperature map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = light
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

for line in lines[i:]:
    if line == "temperature-to-humidity map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = temperature
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

for line in lines[i:]:
    if line == "humidity-to-location map:":
        i += 1
        break
    i += 1

for line in lines[i:]:
    if len(line) == 0:
        i += 1
        break
    next = humidity
    dest, source, l = [int(x) for x in line.split(" ")]
    next[source] = (dest, l)
    i += 1

def lookup(d, i):
    # Find the largest key less than or equal to i
    l = [k for k in d if k <= i]
    if len(l) == 0:
        return i
    the_key = max(l)
    if the_key is None:
        return i
    mapping_start, mapping_len = d[the_key]
    mapping_offset = i - the_key
    if mapping_offset >= mapping_len:
        return i
    return mapping_start + mapping_offset

def lookup_location(i):
    return lookup(humidity, lookup(temperature, lookup(light, lookup(water, lookup(fertilizer, lookup(soil, lookup(seeds, i)))))))

#print(humidity)
#print(temperature)
#print(light)
#print(water)
#print(fertilizer)
#print(soil)
#print(seeds)

locations = [lookup_location(x) for x in initial_seeds]
print(locations)

print(min(locations))