import bisect
import time

from typing import List, Tuple

# from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 9

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


"""
Credits: <https://openwebui.gmacario.it/c/0f329457-55b7-4645-b52e-390fbaaaf94e>

Prompt:

Solve Part One of the following challenge by creating a Python function with the following signature:

```python
def solve_part1_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

Make sure you get the same result as shown in the example.

Here is the full text of the challenge:

(paste contents of day09/README.md)
"""
def solve_part1_with_ai(input_lines: List[str]) -> int:
    """
    Advent of Code 2025 – Day 9, Part 1

    Given a list of coordinate strings "x,y" describing red tiles,
    returns the area of the largest axis‑aligned rectangle whose
    opposite corners are both red tiles.

    The area is counted in tiles and includes the border tiles,
    i.e. width = |dx| + 1, height = |dy| + 1.
    """
    # Parse the coordinates
    points: List[Tuple[int, int]] = []
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split(',')
        points.append((int(x_str), int(y_str)))

    n = len(points)
    if n < 2:
        return 0

    max_area = 0
    # Examine every unordered pair exactly once
    for i in range(n - 1):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


"""
Credits: https://openwebui.gmacario.it/c/97871a03-12da-49d0-9b31-641f547e9b3a

Prompt:

Solve Part Two of the following challenge by creating a Python function with the following signature:

```python
def solve_part2_with_ai(input_lines: List[str]) -> int
```

where `input_lines` is a list of string produced by reading the input file as per the provided example:

Make sure you get the same result as shown in the example.

Here is the full text of the challenge:

(paste contents of day09/README.md)
"""
def solve_part2_with_ai(input_lines: List[str]) -> int:
    # ------------------------------------------------------------------
    # 1. read red points
    # ------------------------------------------------------------------
    reds: List[Tuple[int, int]] = []
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split(',')
        reds.append((int(x_str), int(y_str)))
    n = len(reds)

    # ------------------------------------------------------------------
    # 2. collect vertical edges (x, y1, y2) with y1 < y2
    # ------------------------------------------------------------------
    vertical_edges = []          # list of (x, y_low, y_high)
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]
        if x1 == x2:                     # vertical edge
            if y1 < y2:
                vertical_edges.append((x1, y1, y2))
            else:
                vertical_edges.append((x1, y2, y1))
        # horizontal edges are not needed for the scanline

    # ------------------------------------------------------------------
    # 3. all distinct y‑coordinates that appear among the vertices
    # ------------------------------------------------------------------
    y_coords = sorted({y for (_, y) in reds})

    # ------------------------------------------------------------------
    # 4. for every such y compute interior column intervals
    # ------------------------------------------------------------------
    # intervals[y] = list of (x_left, x_right) that are interior for row y
    y_to_intervals = {}

    for y in y_coords:
        cross = []
        for x, low, high in vertical_edges:
            if low <= y < high:          # row y is intersected by this edge
                cross.append(x)
        cross.sort()
        intervals = []
        for k in range(0, len(cross), 2):
            xl = cross[k]
            xr = cross[k + 1] - 1          # inclusive interior, stop before boundary
            intervals.append((xl, xr))
        y_to_intervals[y] = intervals

    # ------------------------------------------------------------------
    # 4. build segment table – intervals are constant between successive y
    # ------------------------------------------------------------------
    seg_y = []                     # start row of each segment (sorted)
    seg_intervals = []             # same length, each entry is a list of (l,r)

    for y in y_coords:
        seg_y.append(y)
        seg_intervals.append(y_to_intervals[y])

    # ------------------------------------------------------------------
    # 5. helper: obtain the interval list that belongs to a concrete row y
    # ------------------------------------------------------------------
    def intervals_of_row(row_y: int) -> List[Tuple[int, int]]:
        """return interior column intervals for the given row (inclusive)"""
        idx = bisect.bisect_right(seg_y, row_y) - 1
        return seg_intervals[idx]

    # ------------------------------------------------------------------
    # 6. rectangle‑inside test
    # ------------------------------------------------------------------
    def rectangle_is_inside(x1: int, y1: int, x2: int, y2: int) -> bool:
        """True iff the rectangle with opposite corners (x1,y1) and (x2,y2)
           lies completely inside the red+green polygon."""
        xlo, xhi = (x1, x2) if x1 <= x2 else (x2, x1)
        ylo, yhi = (y1, y2) if y1 <= y2 else (y2, y1)

        cur = ylo
        while cur <= yhi:
            seg_idx = bisect.bisect_right(seg_y, cur) - 1
            # end of the current segment (rows share the same intervals)
            if seg_idx + 1 < len(seg_y):
                seg_end = seg_y[seg_idx + 1] - 1
            else:
                seg_end = yhi                 # last segment, we never need +∞
            upper = min(seg_end, yhi)

            # intervals are the same for the whole sub‑range [cur .. upper]
            good = False
            for xl, xr in seg_intervals[seg_idx]:
                if xl <= xlo and xhi <= xr:
                    good = True
                    break
            if not good:
                return False

            cur = upper + 1
        return True

    # ------------------------------------------------------------------
    # 7. search the best rectangle
    # ------------------------------------------------------------------
    best_area = 0
    for i in range(n):
        x1, y1 = reds[i]
        for j in range(i + 1, n):
            x2, y2 = reds[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area <= best_area:          # cannot improve the current best
                continue
            if rectangle_is_inside(x1, y1, x2, y2):
                best_area = area

    return best_area


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
