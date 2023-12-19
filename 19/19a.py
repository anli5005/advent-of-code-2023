import sys
import re
from dataclasses import dataclass

large_parts = sys.stdin.read().split("\n\n")
workflow_strs = large_parts[0].split("\n")
part_strs = large_parts[1].split("\n")

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

workflows = {}

def do_workflow(name: str, p: Part):
    print(f"Executing {name} on {p}")
    global workflows
    workflow = workflows[name]
    for f in workflow:
        result = f(p)
        if result is not None:
            return result
    return None

def evaluate_predicate(predicate_var: str, comparison: str, operand: int, p: Part):
    v = 0
    match predicate_var:
        case "x":
            v = p.x
        case "m":
            v = p.m
        case "a":
            v = p.a
        case "s":
            v = p.s
    match comparison:
        case "=":
            return v == operand
        case "<":
            return v < operand
        case ">":
            return v > operand

for line in workflow_strs:
    start_index = line.index("{")
    name = line[:start_index]
    definition = line[(start_index+1):-1]
    workflow = []
    for item in definition.split(","):
        dest = item.split(":")[1] if ":" in item else item
        if dest == "A":
            dest_function = lambda p: True
        elif dest == "R":
            dest_function = lambda p: False
        else:
            dest_function = lambda p, dest=dest: do_workflow(dest, p)
        if ":" in item:
            item_parts = item.split(":")
            predicate = item_parts[0]
            workflow.append(lambda p, predicate=predicate, dest_function=dest_function: dest_function(p) if evaluate_predicate(predicate[0], predicate[1], int(predicate[2:]), p) else None)
        else:
            workflow.append(dest_function)
    workflows[name] = workflow

print(workflows)
result = 0

for line in part_strs:
    line_parts = line[1:-1].split(",")
    part = Part(int(line_parts[0][2:]), int(line_parts[1][2:]), int(line_parts[2][2:]), int(line_parts[3][2:]))
    answer = do_workflow("in", part)
    print(f"{line} -> {answer}")
    if answer:
        result += part.x + part.m + part.a + part.s

print(result)
