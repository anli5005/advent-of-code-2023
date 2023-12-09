import sys
import re
from functools import cmp_to_key

lines = sys.stdin.read().split("\n")
ranks = list("23456789TJQKA")

def get_type(hand: str):
    card_set = set(hand)
    card_list = list(sorted(card_set, key=lambda x: -hand.count(x)))
    print(card_list)
    # Five of a hand
    if len(card_set) == 1:
        return 5
    if len(card_set) == 2:
        # Four of a hand
        if hand.count(card_list[0]) == 4 and hand.count(card_list[1]) == 1:
            return 4
        # Full house
        if hand.count(card_list[0]) == 3 and hand.count(card_list[1]) == 2:
            return 3
    if len(card_set) == 3:
        # Three of a hand
        if hand.count(card_list[0]) == 3 and hand.count(card_list[1]) == 1 and hand.count(card_list[2]) == 1:
            return 2
        # Two pairs
        if hand.count(card_list[0]) == 2 and hand.count(card_list[1]) == 2 and hand.count(card_list[2]) == 1:
            return 1
    if len(card_set) == 4:
        # One pair
        if hand.count(card_list[0]) == 2 and hand.count(card_list[1]) == 1 and hand.count(card_list[2]) == 1 and hand.count(card_list[3]) == 1:
            return 0
    return -1

def compare_hands(at: str, bt: str) -> int:
    a = at[0]
    b = bt[0]
    a_type = get_type(a)
    b_type = get_type(b)
    print(f"{a} {a_type} {b} {b_type}")
    if a_type > b_type:
        return 1
    elif a_type < b_type:
        return -1
    else:
        for i in range(len(a)):
            if ranks.index(a[i]) > ranks.index(b[i]):
                return 1
            elif ranks.index(a[i]) < ranks.index(b[i]):
                return -1
        return 0

result = 0

hands = [(hand, int(bid)) for hand, bid in [line.split() for line in lines]]
sorted_hands = hands
sorted_hands.sort(key=cmp_to_key(compare_hands))
rank = 1
for i in range(len(sorted_hands)):
    print(f"{sorted_hands[i][0]} {sorted_hands[i][1]} -> {rank}")
    result += sorted_hands[i][1] * rank
    rank += 1

print(result)
