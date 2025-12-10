import collections
import re
import time

from typing import List

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 10

CHALLENGE_URL = f"https://adventofcode.com/{CHALLENGE_YEAR}/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code {CHALLENGE_YEAR} - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, "r") as file:
    input_lines = [line.rstrip() for line in file]

ic(input_lines)


"""
Credits: <https://openwebui.gmacario.it/c/1e6ba280-d187-4389-bd75-f5749352da53>

Prompt:

Solve Part One of the following challenge by creating a Python function with the following signature:

```python
def solve_part1_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

Make sure you get the same result as shown in the example.

Here is the full text of the challenge:

(paste contents of day10/README.md)
"""
def solve_part1_with_ai(input_lines: List[str]) -> int:
    """
    Returns the minimal total number of button presses needed to configure
    all machines described by the given input lines.
    """
    total_presses = 0

    # regular expressions used once per line
    pattern_re = re.compile(r'\[([.#]+)\]')
    buttons_re = re.compile(r'\(([^)]*)\)')

    for raw_line in input_lines:
        line = raw_line.strip()
        if not line:
            continue

        # ----- parse the target pattern -----
        m = pattern_re.search(line)
        if not m:
            raise ValueError(f"Line missing pattern []: {line}")
        pattern = m.group(1)
        n = len(pattern)                     # number of lights

        target = 0
        for i, ch in enumerate(pattern):
            if ch == '#':
                target |= 1 << i

        # ----- parse button masks -----
        button_masks = []
        for btn_text in buttons_re.findall(line):
            btn_text = btn_text.strip()
            if btn_text == '':
                indices = []
            else:
                indices = [int(x) for x in btn_text.split(',') if x != '']
            mask = 0
            for idx in indices:
                mask |= 1 << idx
            button_masks.append(mask)

        # ----- BFS over light configurations -----
        max_state = 1 << n
        dist = [-1] * max_state
        q = collections.deque()

        start = 0
        dist[start] = 0
        q.append(start)

        while q:
            state = q.popleft()
            if state == target:
                break                # reached optimum for this machine
            d = dist[state]
            for bm in button_masks:
                nxt = state ^ bm
                if dist[nxt] == -1:
                    dist[nxt] = d + 1
                    q.append(nxt)

        # after BFS we must have visited the target
        if dist[target] == -1:
            raise RuntimeError("Target configuration unreachable")
        total_presses += dist[target]

    return total_presses


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

(paste contents of day10/README.md)
"""
# def solve_part2_with_ai(input_lines: List[str]) ->int:
#   pass  # TODO


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
