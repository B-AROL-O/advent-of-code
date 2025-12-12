import re
import time

from typing import List, Set, Tuple, FrozenSet

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 12

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
Credits: <https://openwebui.gmacario.it/c/291c2754-fbf8-47dd-8e20-7064e516cab7>

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
# ------------------------------------------------------------
#  Geometry helpers
# ------------------------------------------------------------
def all_orientations(cells: Set[Tuple[int, int]]) -> List[FrozenSet[Tuple[int, int]]]:
    """return all distinct orientations of the shape (rotations + optional mirror)"""
    ic(f"all_orientations(cells={cells})")
    result: Set[FrozenSet[Tuple[int, int]]] = set()
    for rot in range(4):
        # rotate
        if rot == 0:
            cur = {(x, y) for x, y in cells}
        elif rot == 1:
            cur = {(-y, x) for x, y in cells}
        elif rot == 2:
            cur = {(-x, -y) for x, y in cells}
        else:  # rot == 3
            cur = {(y, -x) for x, y in cells}
        for mirror in (False, True):
            if mirror:
                cur2 = {(-x, y) for x, y in cur}
            else:
                cur2 = cur
            # normalize: shift so min x,y become 0
            min_x = min(x for x, _ in cur2)
            min_y = min(y for _, y in cur2)
            norm = frozenset((x - min_x, y - min_y) for x, y in cur2)
            result.add(norm)
    return list(result)


def placements_for_orientation(
    orient: FrozenSet[Tuple[int, int]], width: int, height: int
) -> List[Set[Tuple[int, int]]]:
    """all placements of a single orientation inside the rectangle"""
    ic(f"placements_for_orientation(orient={orient}, width={width}, height={height})")
    max_x = max(x for x, _ in orient)
    max_y = max(y for _, y in orient)
    placements = []
    for ox in range(width - max_x):
        for oy in range(height - max_y):
            cells = {(ox + x, oy + y) for x, y in orient}
            placements.append(cells)
    return placements


# ------------------------------------------------------------
#  Back‑tracking exact cover
# ------------------------------------------------------------
def can_fit_region(
    width: int,
    height: int,
    needed: List[int],
    shape_orients: List[List[FrozenSet[Tuple[int, int]]]],
) -> bool:
    """True iff the region can accommodate the required copies"""

    ic(f"can_fit_region(width={width}, height={height}, needed={needed}, shape_orients={shape_orients})")

    # ---- pre‑compute all placements per shape -----------------
    placements_per_shape: List[List[Set[Tuple[int, int]]]] = []
    for idx, orients in enumerate(shape_orients):
        all_places: List[Set[Tuple[int, int]]] = []
        for orient in orients:
            all_places.extend(placements_for_orientation(orient, width, height))
        placements_per_shape.append(all_places)

    # ---- recursive search ------------------------------------
    needed_counts: List[int] = needed[:]  # mutable copy
    occupied: Set[Tuple[int, int]] = set()

    # simple cache: for a shape we can reuse the list of placements,
    # we only filter them according to the current occupied set.
    def backtrack() -> bool:
        # success ?
        if all(c == 0 for c in needed_counts):
            return True

        # choose the shape with smallest number of still‑possible placements
        best_shape = -1
        best_options: List[Set[Tuple[int, int]]] = []
        for i, cnt in enumerate(needed_counts):
            if cnt == 0:
                continue
            opts = [p for p in placements_per_shape[i] if p.isdisjoint(occupied)]
            if len(opts) < cnt:          # not enough distinct placements
                return False
            if not opts:                 # dead end
                return False
            if best_shape == -1 or len(opts) < len(best_options):
                best_shape = i
                best_options = opts
                if len(best_options) == cnt:   # cannot be better
                    pass

        # try each possible placement for the selected shape
        for place in best_options:
            # place one copy
            occupied.update(place)
            needed_counts[best_shape] -= 1
            if backtrack():
                return True
            # undo
            needed_counts[best_shape] += 1
            occupied.difference_update(place)

        return False

    return backtrack()


# ------------------------------------------------------------
#  Main solver required by the statement
# ------------------------------------------------------------
def solve_part1_with_ai(input_lines: List[str]) -> int:
    """
    Returns the number of regions that can fit all required presents.
    """
    lines = [ln.rstrip("\n") for ln in input_lines]

    # ---------- parse shapes ----------
    shape_cells: List[Set[Tuple[int, int]]] = []
    i = 0
    shape_header = re.compile(r"^(\d+):\s*$")
    region_header = re.compile(r"^\d+x\d+:")
    while i < len(lines):
        m = shape_header.match(lines[i])
        if not m:
            break
        # start a new shape
        i += 1
        y = 0
        cells: Set[Tuple[int, int]] = set()
        while i < len(lines):
            if shape_header.match(lines[i]) or region_header.match(lines[i]):
                break
            line = lines[i]
            for x, ch in enumerate(line):
                if ch == "#":
                    cells.add((x, y))
            y += 1
            i += 1
        shape_cells.append(cells)

    # pre‑compute orientations for every shape
    shape_orients: List[List[FrozenSet[Tuple[int, int]]]] = [
        all_orientations(cells) for cells in shape_cells
    ]

    # ---------- parse regions ----------
    region_re = re.compile(r"^(\d+)x(\d+):\s*(.*)$")
    answer = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        m = region_re.match(line)
        if not m:
            continue  # ignore malformed lines (should not happen)
        w, h, rest = int(m.group(1)), int(m.group(2)), m.group(3).strip()
        counts = list(map(int, rest.split()))
        # safety: pad with zeros if input omitted trailing zeros
        if len(counts) < len(shape_cells):
            counts.extend([0] * (len(shape_cells) - len(counts)))

        if can_fit_region(w, h, counts, shape_orients):
            answer += 1

    return answer


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
