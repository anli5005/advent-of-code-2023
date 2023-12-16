import sys
import re

lines = sys.stdin.read().split("\n")
grid = [list(line) for line in lines]
energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

result = 0

already_encountered = set()
beams = [((0, 0), (0, 1))]

while beams:
    current_beams = list(beams)
    beams = []
    for beam in current_beams:
        pos, direction = beam
        already_encountered.add(beam)
        energized[pos[0]][pos[1]] = True
        next_directions = []
        tile = grid[pos[0]][pos[1]]
        if tile == ".":
            next_directions.append(direction)
        elif tile == "/":
            if direction == (0, 1):
                next_directions.append((-1, 0))
            elif direction == (0, -1):
                next_directions.append((1, 0))
            elif direction == (1, 0):
                next_directions.append((0, -1))
            elif direction == (-1, 0):
                next_directions.append((0, 1))
        elif tile == "\\":
            if direction == (0, 1):
                next_directions.append((1, 0))
            elif direction == (0, -1):
                next_directions.append((-1, 0))
            elif direction == (1, 0):
                next_directions.append((0, 1))
            elif direction == (-1, 0):
                next_directions.append((0, -1))
        elif tile == "|":
            if direction[0] == 0:
                next_directions.append((1, 0))
                next_directions.append((-1, 0))
            else:
                next_directions.append(direction)
        elif tile == "-":
            if direction[1] == 0:
                next_directions.append((0, 1))
                next_directions.append((0, -1))
            else:
                next_directions.append(direction)
        for next_direction in next_directions:
            next_pos = (pos[0] + next_direction[0], pos[1] + next_direction[1])
            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]):
                continue
            new_beam = (next_pos, next_direction)
            if new_beam in already_encountered:
                continue
            beams.append(new_beam)

print(sum([sum([1 if energized[i][j] else 0 for j in range(len(grid[0]))]) for i in range(len(grid))]))
