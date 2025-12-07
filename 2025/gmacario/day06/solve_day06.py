import operator
import time

from functools import reduce
from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 6

CHALLENGE_URL = f"https://adventofcode.com/{CHALLENGE_YEAR}/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code {CHALLENGE_YEAR} - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, "r") as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)


def product(iterable):
    """Return the product of the numbers in iterable."""
    return reduce(operator.mul, iterable, 1)


def solve_part1_by_gpt_oss_120(raw_lines) -> int:
    # # ---------- read and pad input ----------
    # raw_lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
    # if not raw_lines:
    #     print(0)
    #     return

    height = len(raw_lines)
    width = max(len(line) for line in raw_lines)
    # pad each line to the same width with spaces
    lines = [line.ljust(width) for line in raw_lines]

    # ---------- find blank columns ----------
    col_is_blank = [all(line[col] == ' ' for line in lines) for col in range(width)]

    # ---------- split into problem column intervals ----------
    intervals = []                     # list of (left, right) inclusive
    col = 0
    while col < width:
        # skip blank columns
        while col < width and col_is_blank[col]:
            col += 1
        if col >= width:
            break
        start = col
        # walk through a block of non‑blank columns
        while col < width and not col_is_blank[col]:
            col += 1
        end = col - 1
        intervals.append((start, end))

    grand_total = 0

    # ---------- solve each problem ----------
    for left, right in intervals:
        # ic(left, right)
        operands = []
        op = None
        for line in lines:
            # ic(line)
            slice_ = line[left:right + 1]
            token = slice_.strip()
            # ic(token)
            if not token:
                continue
            if token == '+' or token == '*':
                op = token
            else:
                operands.append(int(token))
                # ic(operands)

        if op == '+':
            result = sum(operands)
        else:               # op == '*'
            result = product(operands)

        grand_total += result
        # ic(result, grand_total)

    return grand_total


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")
    result_part1 = solve_part1_by_gpt_oss_120(input_lines)

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
