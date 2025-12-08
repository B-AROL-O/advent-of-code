import time

from collections import deque
from typing import List

# from icecream import ic

CHALLENGE_DAY = 4

CHALLENGE_URL = f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  CHALLENGE_URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, "r") as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)


"""
Credits: <https://openwebui.gmacario.it/c/c19b36fc-d4fe-4bdc-9ca9-f6b178edf237>

Prompt:

Solve Part Two of the following challenge by creating a Python function with the following signature:

```python
def solve_part2_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

(paste contents of day04/sample_day04.txt)

Here is the full text of the challenge:

(paste contents of day04/README.md)
"""
def solve_part2_with_ai(input_lines: List[str]) -> int:
    """
    Implements the Part 2 solution described above.
    Returns the total number of '@' cells that can be removed.
    """
    if not input_lines:
        return 0

    rows = len(input_lines)
    cols = len(input_lines[0])

    # 1. parse the grid
    paper = [[c == '@' for c in line] for line in input_lines]

    # 2. auxiliary structures
    removed = [[False] * cols for _ in range(rows)]
    deg = [[0] * cols for _ in range(rows)]

    # 8 possible neighbour offsets
    neigh_offsets = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]

    # 3. initial degree computation
    for i in range(rows):
        for j in range(cols):
            if not paper[i][j]:
                continue
            cnt = 0
            for di, dj in neigh_offsets:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and paper[ni][nj]:
                    cnt += 1
            deg[i][j] = cnt

    # 4. initialise queue with cells of degree < 4
    q = deque()
    for i in range(rows):
        for j in range(cols):
            if paper[i][j] and deg[i][j] < 4:
                q.append((i, j))

    removed_cnt = 0

    # 5. iterative removal
    while q:
        i, j = q.popleft()
        if removed[i][j]:
            continue            # may have been queued earlier
        removed[i][j] = True
        removed_cnt += 1

        # decrease degree of still‑present neighbours
        for di, dj in neigh_offsets:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if paper[ni][nj] and not removed[ni][nj]:
                    deg[ni][nj] -= 1
                    # we only need to enqueue when it just crossed the threshold
                    if deg[ni][nj] == 3:
                        q.append((ni, nj))

    return removed_cnt


def solve_part1():
    tm_start = time.time()
    # result_part1 = 0
    # ic("DEBUG: TODO solve_part1()")

    # Credits: gpt-oss:120b on <https://openwebui.gmacario.it>
    #
    # Prompt:
    #   Solve this challenge using Python:
    #   (paste README.md)
    #
    def solve(grid: list) -> int:
        # # read the whole input, keep line order, strip trailing newlines
        # grid = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']
        # if not grid:
        #     print(0)
        #     return

        R = len(grid)
        C = len(grid[0])
        # ic(R, C)

        answer = 0
        # directions for the eight neighbours
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for r in range(R):
            row = grid[r]
            for c in range(C):
                if row[c] != "@":
                    continue  # not a roll of paper

                cnt = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == "@":
                            cnt += 1
                if cnt < 4:
                    answer += 1
        return answer

    result_part1 = solve(input_lines)
    # ic(result_part1)

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
    # check_valid_id_part2("1010")
    # check_valid_id_part2("1011")
    solve_part2()
    pass

# EOF
