import sys
from collections import Counter

lines = sys.stdin.read().split("\n")
unfold = True

result = 0

num_proc = 0
for line in lines:
    parts = line.split()

    if unfold:
        springs = "?".join([parts[0]] * 5)
        expected = [int(x) for x in parts[1].split(",")] * 5
    else:
        springs = parts[0]
        expected = [int(x) for x in parts[1].split(",")]

    # dp[i][j] = number of arrangements from the first j springs that
    #            correspond to the first i expected amounts
    dp = [[] for _ in range(len(expected))]
    
    # Base case: dp[0]
    for j in range(len(springs) + 1):
        if j < len(springs) and springs[j] == "#":
            dp[0].append(0)
            continue
        start_index = j - expected[0]
        if start_index < 0:
            dp[0].append(0)
            continue
        if sum([1 for ch in springs[start_index:j] if ch == "#" or ch == "?"]) == expected[0]:
            if all(ch == "." or ch == "?" for ch in springs[0:start_index]):
                dp[0].append(1)
                continue
        dp[0].append(0)
    
    for i in range(1, len(expected)):
        for j in range(len(springs) + 1):
            dp_result = 0
            for k in range(j - 1):
                if j < len(springs) and springs[j] == "#":
                    continue
                start_index = j - expected[i]
                if start_index <= k:
                    continue
                if sum([1 for ch in springs[start_index:j] if ch == "#" or ch == "?"]) == expected[i]:
                    if all(ch == "." or ch == "?" for ch in springs[k:start_index]):
                        dp_result += dp[i - 1][k]
                        continue
            dp[i].append(dp_result)

    answer = 0
    for i in range(len(springs), -1, -1):
        if i < len(springs) and springs[i] == "#":
            break
        answer += dp[-1][i]

    print(f"{num_proc} {line} {answer} <- {dp[-1]}")
    result += answer
    num_proc += 1

print(result)
