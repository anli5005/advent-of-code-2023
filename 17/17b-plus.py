# 17b.py, but using A* with a simple taxicab heuristic
# Touches fewer states but runs slower, probably because the heuristic
# doesn't provide terribly useful info

import sys
from queue import PriorityQueue

lines = sys.stdin.read().split("\n")
grid = [[int(c) for c in line] for line in lines]

result = 0

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def heuristic(state):
    pos = state[0]
    return len(grid) - pos[0] - 1 + len(grid[0]) - pos[1] - 1

# (heuristic, loss, state = (pos, direction, so far))
pq = PriorityQueue()
initial_states = [((0, 0), 0, 0), ((0, 0), 1, 0)]
for state in initial_states:
    pq.put((heuristic(state), 0, state))

seen = set()
while not pq.empty():
    h, loss, state = pq.get()
    if state in seen:
        continue
    seen.add(state)
    pos, direction, so_far = state
    i, j = pos
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        result = loss
        break
    directions = []
    if so_far < 10:
        directions.append(direction)
    if so_far >= 4:
        directions.append((direction + 1) % 4)
        directions.append((direction + 3) % 4)
    for nd in directions:
        di, dj = dir[nd]
        ni = i + di
        nj = j + dj
        if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]):
            next_so_far = so_far + 1 if direction == nd else 1
            next_loss = loss + grid[ni][nj]
            next_state = ((ni, nj), nd, next_so_far)
            pq.put((next_loss + heuristic(next_state), next_loss, next_state))

print(f"Seen {len(seen)} states")
print(result)
