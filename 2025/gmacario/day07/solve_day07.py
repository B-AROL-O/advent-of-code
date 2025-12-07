import time

from collections import deque

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 7

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

grid = []
row = 0
start_pos = (-1, -1)  # Start with invalid position
for line in input_lines:
    ic(line)
    buf = []
    for col in range(len(line)):
        ch = line[col:col+1]
        assert ch in ['S', '^', '.']
        buf.append(ch)
        if ch == "S":
            assert start_pos == (-1, -1)
            start_pos = (row, col)
        # elif ch == ".":
        #     pass
        # elif ch == "^":
        #     pass
        # else:
        #     ic(f"ERROR: Unhandled ch={ch} at {(row, col)}")

    grid.append(buf)
    col += 1
assert not start_pos == (-1, -1)

ic(grid)
ic(grid[0][7])

# Credits: <https://openwebui.gmacario.it/c/f5029843-7219-49a2-b8b4-439d364fc1b1>
#   - Server: <https://openwebui.gmacario.it>
#   - OpenWebUI: v0.6.41
#   - Ollama: 0.13.1
#   - Model: gpt-oss:120b
#
# Prompt:
#   Solve using Python
#   (paste contents of README.md)
def solve_beams(grid, start_row, start_col):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    q.append((start_row, start_col))
    splits = 0
    
    while q:
        r, c = q.popleft()
        if r >= rows or c < 0 or c >= cols:
            continue  # Skip if out of bounds
        cell = grid[r][c]
        if cell == '^':
            splits += 1
            q.append((r+1, c))
            q.append((r+1, c))
        else:  # cell == '.'
            q.append((r+1, c))
    return splits


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    ic("DEBUG: TODO solve_part1()")
    result_part1 = solve_beams(grid, start_pos[0], start_pos[1])

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
