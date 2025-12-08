from __future__ import annotations
import time

from collections import deque
from functools import lru_cache
from typing import List

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 7

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

# SANITY CHECKS ON input_lines
#
# grid = []
# row = 0
# start_pos = (-1, -1)  # Start with invalid position
# for line in input_lines:
#     ic(line)
#     buf = []
#     for col in range(len(line)):
#         ch = line[col:col+1]
#         assert ch in ['S', '^', '.']
#         buf.append(ch)
#         if ch == "S":
#             assert start_pos == (-1, -1)
#             start_pos = (row, col)
#         # elif ch == ".":
#         #     pass
#         # elif ch == "^":
#         #     pass
#         # else:
#         #     ic(f"ERROR: Unhandled ch={ch} at {(row, col)}")
#
#     grid.append(buf)
#     col += 1
# assert not start_pos == (-1, -1)
#
# ic(grid)
# ic(grid[0][7])

# Thanks to AI: <https://openwebui.gmacario.it/c/f5029843-7219-49a2-b8b4-439d364fc1b1>
#   - Server: <https://openwebui.gmacario.it>
#   - OpenWebUI: v0.6.41
#   - Ollama: 0.13.1
#   - Model: gpt-oss:120b
#
# Prompt:
#   Solve using Python
#   (paste contents of README.md)
#
# Plus some HI to implement manual corrections
#
def solve_beams(grid, start_row, start_col):
    # ic(f"solve_beams(grid, start_row={start_row}, start_col={start_col})")
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    q.append((start_row, start_col))
    splits = 0
    
    while q:
        # ic(q)
        r, c = q.popleft()
        if r >= rows or c < 0 or c >= cols:
            continue  # Skip if out of bounds
        cell = grid[r][c]
        if cell == '^':
            splits += 1
            # ic(f"new splits={splits}")
            # Each '^' splits into two downward beams
            if c - 1 >= 0 and q.count((r+1, c-1)) == 0:
                q.append((r+1, c-1))
            if c + 1 < cols  and q.count((r+1, c+1)) == 0:
                q.append((r+1, c+1))
        else:  # cell == '.'
            # Continue downward with one beam
            if q.count((r+1, c)) == 0:
                q.append((r+1, c))
    return splits


"""
Credits: TODO

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
def solve_part2_with_ai(input_lines: List[str]) -> int:
    """
    Returns the number of different timelines produced by a single tachyon
    particle travelling through the quantum tachyon manifold described by
    `input_lines`.
    """
    grid = [line.rstrip('\n') for line in input_lines]
    H = len(grid)
    if H == 0:
        return 0
    W = len(grid[0])

    # locate the start cell 'S'
    sr = sc = -1
    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            sr, sc = r, c
            break
    if sr == -1:
        raise ValueError("No start cell 'S' found in input")

    @lru_cache(maxsize=None)
    def ways(r: int, c: int) -> int:
        """
        Number of timelines that start in cell (r,c) and eventually exit.
        The cell (r,c) is guaranteed to be '.' or 'S'.
        """
        # move straight down while the cells are empty
        rr = r + 1
        while rr < H and grid[rr][c] == '.':
            rr += 1

        # reached the bottom -> the particle leaves the manifold
        if rr == H:
            return 1

        # we are on a splitter at (rr, c)
        total = 0
        # left branch
        if c - 1 >= 0:
            total += ways(rr, c - 1)
        else:
            # left would be outside the diagram → immediate exit
            total += 1
        # right branch
        if c + 1 < W:
            total += ways(rr, c + 1)
        else:
            total += 1
        return total

    return ways(sr, sc)


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")
    result_part1 = solve_beams(input_lines, 0, input_lines[0].index('S'))

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
