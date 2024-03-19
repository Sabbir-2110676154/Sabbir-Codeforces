import math

def calculate_min_tents(introverts, extroverts, universals):
    leftover_extroverts = extroverts % 3
    if leftover_extroverts + universals >= 3 or leftover_extroverts == 0:
        return introverts + math.ceil((extroverts + universals) / 3)
    else:
        return -1

test_cases = int(input())

for _ in range(test_cases):
    introverts, extroverts, universals = map(int, input().split())
    min_tents = calculate_min_tents(introverts, extroverts, universals)
    print(min_tents)