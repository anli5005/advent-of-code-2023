import sys
from queue import Queue
from collections import defaultdict

lines = sys.stdin.read().split("\n")
broadcasters = defaultdict(lambda: (0, []))
connections = defaultdict(lambda: [])

for line in lines:
    parts = line.split(" -> ")
    if parts[0] == "broadcaster":
        name = parts[0]
        type = 0
    elif parts[0][0] == "%":
        name = parts[0][1:]
        type = 1
    elif parts[0][0] == "&":
        name = parts[0][1:]
        type = 2
    triggers = parts[1].split(", ")
    broadcasters[name] = (type, triggers)
    for trigger in triggers:
        connections[trigger] = connections[trigger] + [name]

result = 0
low = 0
high = 0

state = defaultdict(lambda: False)

for i in range(1000):
    enqueued_pulses = Queue()
    enqueued_pulses.put(("broadcaster", False, "button"))
    while not enqueued_pulses.empty():
        current = enqueued_pulses.get()
        if current[1]:
            high += 1
        else:
            low += 1
        name = current[0]
        broadcaster = broadcasters[name]
        match broadcaster[0]:
            case 0:
                next_pulse = current[1]
            case 1:
                if current[1]:
                    continue
                state[name] = not state[name]
                next_pulse = state[name]
            case 2:
                if not state[name]:
                    state[name] = {connection: False for connection in connections[name]}
                state[name][current[2]] = current[1]
                next_pulse = not all(state[name][k] for k in state[name])
        for trigger in broadcaster[1]:
            enqueued_pulses.put((trigger, next_pulse, name))

result = low * high
print(f"{low} * {high} -> {result}")
