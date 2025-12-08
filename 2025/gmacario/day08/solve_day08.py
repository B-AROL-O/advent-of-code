import time

from typing import List, Tuple

from icecream import ic

CHALLENGE_YEAR = 2025
CHALLENGE_DAY = 8

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


# Credits: <https://openwebui.gmacario.it/c/602f14ab-20cf-4ee3-97e3-9d723ff2c845>
#
class DSU:
    """Disjoint‑Set Union with size tracking."""
    __slots__ = ("parent", "size")

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n               # size is valid only at a root

    def find(self, x: int) -> int:
        # iterative path‑compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        # ic(f"union({self}, {a}, {b})")
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return                        # already in the same component
        # union by size – attach the smaller tree under the larger one
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        # ic(f"sorted ra={ra}, rb={rb}")
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        # ic(f"new self.parent[{rb}]={ra}, self.size[{ra}]={self.size[ra]}")


def solve_day08_ai(input_lines: List[str]) -> int:
    """
    Returns the product of the sizes of the three largest circuits after
    joining the 1000 closest pairs of points described by `input_lines`.

    Parameters
    ----------
    input_lines :
        List of strings, each of the form "x,y,z". Empty strings are ignored.

    Returns
    -------
    int
        size₁ × size₂ × size₃ where size₁ ≥ size₂ ≥ size₃ are the three
        largest component sizes.
    """
    # ------------------------------------------------------------------
    # 1. Parse the points
    # ------------------------------------------------------------------
    points: List[Tuple[int, int, int]] = []
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(','))
        points.append((x, y, z))

    n = len(points)
    # ic(n)
    if n == 0:
        return 0                       # degenerate case – nothing to connect

    # ------------------------------------------------------------------
    # 2. Build the complete edge list (distance², i, j)
    # ------------------------------------------------------------------
    edges: List[Tuple[int, int, int]] = []
    for i in range(n):
        xi, yi, zi = points[i]
        for j in range(i + 1, n):
            xj, yj, zj = points[j]
            d2 = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
            edges.append((d2, i, j))
    # ic(edges)

    # ------------------------------------------------------------------
    # 3. Sort edges by distance (squared)
    # ------------------------------------------------------------------
    edges.sort(key=lambda e: e[0])
    # ic(edges)

    # ------------------------------------------------------------------
    # 4. Perform the first 1000 unions (or fewer if the graph has <1000 edges)
    # ------------------------------------------------------------------
    dsu = DSU(n)
    limit = min(1000, len(edges))
    for k in range(limit):
        _, a, b = edges[k]
        dsu.union(a, b)
    # ic(dsu)

    # ------------------------------------------------------------------
    # 5. Gather component sizes
    # ------------------------------------------------------------------
    comp_sizes = {}
    for i in range(n):
        root = dsu.find(i)
        # size is stored at the root; we only need to store it once
        comp_sizes[root] = dsu.size[root]
        # ic(root, comp_sizes[root])
    # ic(comp_sizes)

    sizes = sorted(comp_sizes.values(), reverse=True)
    # ic(sizes)

    # The puzzle guarantees at least three components, but we guard anyway.
    while len(sizes) < 3:
        sizes.append(1)

    # ------------------------------------------------------------------
    # 6. Return the product of the three largest sizes
    # ------------------------------------------------------------------
    # ic(sizes)
    return sizes[0] * sizes[1] * sizes[2]


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")
    result_part1 = solve_day08_ai(input_lines)

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
