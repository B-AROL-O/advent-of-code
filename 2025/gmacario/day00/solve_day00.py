import time

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 0  # TODO: Adjust

CHALLENGE_URL = f"https://adventofcode.com/{CHALLENGE_YEAR}/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
# INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code {CHALLENGE_YEAR} - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, "r") as file:
    input_lines = [line.rstrip() for line in file]

ic(input_lines)


"""
Credits: TODO

Prompt:

Solve Part One of the following challenge by creating a Python function with the following signature:

```python
def solve_part1_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

Make sure you get the same result as shown in the example.

Here is the full text of the challenge:

(paste contents of daynn/README.md)
"""
# def solve_part1_with_ai(input_lines: List[str]) ->int:
#   pass  # TODO


"""
Credits: TODO

Prompt:

Solve Part Two of the following challenge by creating a Python function with the following signature:

```python
def solve_part2_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

Make sure you get the same result as shown in the example.

Here is the full text of the challenge:

(paste contents of daynn/README.md)
"""
# def solve_part2_with_ai(input_lines: List[str]) ->int:
#   pass  # TODO


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    ic("DEBUG: TODO solve_part1()")
    # result_part1 = solve_part1_with_ai(input_lines)

    tm_end = time.time()
    print(f"DEBUG: solve_part1 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part1 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part1 Delta: {tm_end - tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    tm_start = time.time()
    result_part2 = 0

    ic("DEBUG: TODO solve_part2()")
    # result_part2 = solve_part2_with_ai(input_lines)

    tm_end = time.time()
    print(f"DEBUG: solve_part2 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part2 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part2 Delta: {tm_end - tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part2 result: {result_part2}")
    return result_part2


if __name__ == "__main__":
    solve_part1()
    solve_part2()

# EOF
