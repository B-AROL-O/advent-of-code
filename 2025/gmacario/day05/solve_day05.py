import time

# from icecream import ic

CHALLENGE_DAY = 5

CHALLENGE_URL = f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, "r") as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)

fresh_ingredients = []
available_ingredients = []
find_fresh_ingredients = True

for line in input_lines:
    if line == "":
        find_fresh_ingredients = False
        continue

    if find_fresh_ingredients:
        fresh_ingredients.append(
            {"from": int(line.split("-")[0]), "to": int(line.split("-")[1])}
        )
    else:
        available_ingredients.append(int(line))

# ic(fresh_ingredients)
# ic(available_ingredients)


"""
Credits: <https://openwebui.gmacario.it/c/aa5b67d6-ccb6-4b66-a94f-914f2ba46d67>

Prompt:

Solve Part Two of the following challenge by creating a Python function with the following signature:

```python
def solve_part2_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

(paste contents of day07/sample_day07.txt)

Here is the full text of the challenge:

(paste contents of day07/README.md)
"""
from typing import List

def solve_part2_with_ai(input_lines: List[str]) -> int:
    """
    Counts how many distinct integer IDs are covered by the fresh‑ID ranges
    appearing before the first blank line of the input.
    """
    # -----------------------------------------------------------------
    # 1. read the ranges (stop at the first blank line)
    ranges = []
    for line in input_lines:
        if line.strip() == "":
            break
        low_str, high_str = line.split('-')
        low, high = int(low_str), int(high_str)
        ranges.append((low, high))

    if not ranges:                # no ranges at all
        return 0

    # -----------------------------------------------------------------
    # 2. sort by lower bound
    ranges.sort(key=lambda p: p[0])

    # 3. merge overlapping / adjacent intervals
    merged = []
    cur_low, cur_high = ranges[0]

    for low, high in ranges[1:]:
        if low <= cur_high + 1:                # overlap or directly adjacent
            if high > cur_high:
                cur_high = high
        else:
            merged.append((cur_low, cur_high))
            cur_low, cur_high = low, high

    merged.append((cur_low, cur_high))          # add the last interval

    # -----------------------------------------------------------------
    # 4. sum their lengths
    total = sum(high - low + 1 for low, high in merged)
    return total


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")

    for id in available_ingredients:
        # ic(f"checking freshness of {id}")
        for r in fresh_ingredients:
            if r["from"] <= id <= r["to"]:
                # ic(f"ingredient {id} is fresh")
                result_part1 += 1
                break
            # ic(f"ingredient {id} is spoiled according to {r}")

    tm_end = time.time()
    print(f"DEBUG: solve_part1 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part1 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part1 Delta: {tm_end - tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    tm_start = time.time()
    result_part2 = 0

    # ic("DEBUG: TODO solve_part2()")
    result_part2 = solve_part2_with_ai(input_lines)

    tm_end = time.time()
    print(f"DEBUG: solve_part2 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part2 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part2 Delta: {tm_end - tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part2 result: {result_part2}")
    return result_part2


if __name__ == "__main__":
    solve_part1()
    solve_part2()
    pass

# EOF
