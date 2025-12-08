import operator
import time

from functools import reduce
from typing import List

# from icecream import ic

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


# Credits: <https://openwebui.gmacario.it/c/f3c5e014-6341-40c1-be55-6e5307c065b5>
# plus some minor modifications by gmacario
#
def solve_part1_with_ai(raw_lines) -> int:
    # # ---------- read and pad input ----------
    # raw_lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
    # if not raw_lines:
    #     print(0)
    #     return

    # height = len(raw_lines)
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


"""
Credits: <https://openwebui.gmacario.it/c/34a8413b-0fbe-479f-838a-feb19121c791>

Prompt:

Solve Part Two of the following challenge by creating a Python function with the following signature:

```python
def solve_part2_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

(paste contents of sample_day06.txt)

Here is the full text of the challenge:

(paste contents of README.md)
"""
def solve_part2_with_ai(input_lines: List[str]) -> int:
    """
    Solve Advent of Code 2025 – Day 6, Part 2.

    Parameters
    ----------
    input_lines : List[str]
        The worksheet lines exactly as read from the input file.

    Returns
    -------
    int
        The grand total – the sum of the results of all individual problems.
    """
    if not input_lines:
        return 0

    # ------------------------------------------------------------------
    # 1. Build a rectangular grid (pad with spaces on the right)
    # ------------------------------------------------------------------
    rows = len(input_lines)
    cols = max(len(line) for line in input_lines)
    grid = [list(line.ljust(cols)) for line in input_lines]  # rows × cols
    # ic(rows,cols)
    # ic(grid)

    # ------------------------------------------------------------------
    # 2. Find column intervals that belong to a single problem
    # ------------------------------------------------------------------
    problems: List[tuple[int, int]] = []          # (start, end) exclusive
    col = 0
    while col < cols:
        # Is column col completely empty?
        if all(grid[r][col] == ' ' for r in range(rows)):
            col += 1
            continue

        start = col
        while col < cols and not all(grid[r][col] == ' ' for r in range(rows)):
            col += 1
        end = col                                   # first empty column after the block
        problems.append((start, end))
    # ic(problems)

    # ------------------------------------------------------------------
    # 3. Evaluate each problem and accumulate the grand total
    # ------------------------------------------------------------------
    grand_total = 0

    for start, end in problems:
        # ic(start, end)
        numbers: List[int] = []

        # rows 0 .. rows-2 contain the numbers
        for c in range(start, end):
            token = ''.join(grid[r][c] for r in range(rows - 1)).strip()
            if token:                     # ignore completely empty rows (should not happen)
                numbers.append(int(token))
        # ic(numbers)

        # last row contains the operator
        op_token = ''.join(grid[rows - 1][c] for c in range(start, end)).strip()
        # ic(op_token)
        if op_token == '+':
            value = sum(numbers)
        elif op_token == '*':
            # product – avoid math.prod for Python <3.8 compatibility
            prod = 1
            for n in numbers:
                prod *= n
            value = prod
        else:
            raise ValueError(f'Unexpected operator {op_token!r} in columns {start}-{end-1}')

        # ic(value)
        grand_total += value

    return grand_total


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")
    result_part1 = solve_part1_with_ai(input_lines)

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

# EOF
