from __future__ import annotations
import collections
import re
import sys
import time

from functools import lru_cache
from typing import List, Tuple

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 10

CHALLENGE_URL = f"https://adventofcode.com/{CHALLENGE_YEAR}/day/{CHALLENGE_DAY}"
INPUT_FILE = f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
# INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code {CHALLENGE_YEAR} - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

# ic()

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
Credits: <https://openwebui.gmacario.it/c/c6961b6d-db49-43a1-b91b-e98d3a87a4e2>

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
INF = 10 ** 9


def min_presses(buttons: List[List[int]], target: List[int]) -> int:
    """
    Return the smallest number of button presses that reach `target`
    starting from the zero vector.
    `buttons[i]` is the list of counters touched by button i.
    """
    if not target:
        return 0

    # sort buttons – big ones first – helps pruning
    buttons = sorted(buttons, key=lambda b: -len(b))
    n = len(buttons)
    m = len(target)

    # pre‑compute the maximal size among the remaining buttons for the bound
    max_button_size_suffix = [0] * (n + 1)
    cur = 0
    for i in range(n - 1, -1, -1):
        cur = max(cur, len(buttons[i]))
        max_button_size_suffix[i] = cur

    @lru_cache(maxsize=None)
    def dfs(i: int, remaining: Tuple[int, ...]) -> int:
        """minimum extra presses using buttons i … n-1"""
        if i == n:
            # all counters must already be satisfied
            return 0 if all(v == 0 for v in remaining) else INF

        # quick impossibility test: if a counter still >0 and no later button touches it
        later_masks = buttons[i:]
        touched = set()
        for mask in later_masks:
            touched.update(mask)
        for idx, val in enumerate(remaining):
            if val > 0 and idx not in touched:
                return INF

        mask = buttons[i]
        # how many times may we press this button?
        if mask:
            max_k = min(remaining[j] for j in mask)
        else:
            max_k = 0

        best = INF

        # pre‑compute the size used for the lower bound
        size_max = max_button_size_suffix[i]

        for k in range(max_k + 1):
            # compute new remaining vector
            if k == 0:
                new_rem = remaining
            else:
                lst = list(remaining)
                for j in mask:
                    lst[j] -= k
                new_rem = tuple(lst)

            # cheap lower bound (Lemma 2)
            if k == 0 and best == INF:
                # we have not found any solution yet – no bound possible
                pass
            else:
                # bound = max( max(new_rem), ceil(sum(new_rem) / size_max) )
                max_need = max(new_rem)
                sum_need = sum(new_rem)
                bound = max_need
                if size_max > 0:
                    bound = max(bound, (sum_need + size_max - 1) // size_max)
                if k + bound >= best:
                    # cannot beat current best
                    continue

            sub = dfs(i + 1, new_rem)
            if sub != INF:
                total = k + sub
                if total < best:
                    best = total
                    # perfect solution found – cannot be improved further
                    if best == 0:
                        break

        return best

    ans = dfs(0, tuple(target))
    # the puzzle guarantees a solution
    return ans


def solve_part2_with_ai(input_lines: List[str]) -> int:
    total = 0
    for line in input_lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        # first part is the indicator lights – ignore it
        idx = 1
        buttons: List[List[int]] = []
        while idx < len(parts) and parts[idx].startswith('('):
            token = parts[idx]
            inside = token.strip('()')
            if inside == '':
                btn = []
            else:
                btn = list(map(int, inside.split(',')))
            buttons.append(btn)
            idx += 1

        # the remaining part is the target vector inside {}
        target_token = parts[idx]
        inside = target_token.strip('{}')
        if inside == '':
            target = []
        else:
            target = list(map(int, inside.split(',')))

        total += min_presses(buttons, target)

    return total


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
