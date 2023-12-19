import sys
from functools import reduce

large_parts = sys.stdin.read().split("\n\n")
workflow_strs = large_parts[0].split("\n")

workflows = {}

def filter_degenerates(parts: list):
    return [(p, t) for p, t in parts if all(r[0] <= r[1] for r in p)]

def evaluate_predicate(predicate_var: str, comparison: str, v: int, p):
    index = "xmas".index(predicate_var)
    r = p[index]
    print(p)
    def rewrite_range(new_r):
        new_p = list(p)
        new_p[index] = new_r
        return new_p
    
    match comparison:
        case "=":
            if v >= r[0] and v <= r[1]:
                return filter_degenerates([
                    (rewrite_range((r[0], v - 1)), False),
                    (rewrite_range((v, v)), False),
                    (rewrite_range((v + 1, r[1])), False)
                ])
            else:
                return [(p, False)]
        case "<":
            if v >= r[0] and v <= r[1]:
                return filter_degenerates([
                    (rewrite_range((r[0], v - 1)), True),
                    (rewrite_range((v, r[1])), False),
                ])
            elif v > r[1]:
                return [(p, True)]
            else:
                return [(p, False)]
        case ">":
            if v >= r[0] and v <= r[1]:
                return filter_degenerates([
                    (rewrite_range((r[0], v)), False),
                    (rewrite_range((v + 1, r[1])), True),
                ])
            elif v > r[1]:
                return [(p, False)]
            else:
                return [(p, True)]

def do_workflow(name: str, p):
    if name == "A":
        return [p]
    elif name == "R":
        return []

    global workflows
    workflow = workflows[name]
    current = [p]
    result = []
    for predicate, dest in workflow:
        new_current = []
        for c in current:
            branches = predicate(c)
            for new_p, succeeded in branches:
                if succeeded:
                    result.extend(do_workflow(dest, new_p))
                else:
                    new_current.append(new_p)
        current = new_current
    
    if len(current) > 0:
        print(f"Warning: len(current) = {len(current)}")
    
    return result

for line in workflow_strs:
    start_index = line.index("{")
    name = line[:start_index]
    definition = line[(start_index+1):-1]
    workflow = []
    for item in definition.split(","):
        dest = item.split(":")[1] if ":" in item else item
        if ":" not in item:
            predicate_func = lambda p: [(p, True)]
        else:
            predicate = item.split(":")[0]
            predicate_func = lambda p, predicate=predicate: evaluate_predicate(predicate[0], predicate[1], int(predicate[2:]), p)
        workflow.append((predicate_func, dest))
    workflows[name] = workflow

result = 0

initial_part = [(1, 4000)] * 4
workflow_res = do_workflow("in", initial_part)
print(workflow_res)

result = sum(reduce(lambda acc, r: acc * (r[1] - r[0] + 1), p, 1) for p in workflow_res)
print(result)
