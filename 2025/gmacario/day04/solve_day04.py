import time

from icecream import ic

CHALLENGE_DAY=4

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  CHALLENGE_URL: {CHALLENGE_URL}")
print(f"INFO:  INPUT_FILE: {INPUT_FILE}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, 'r') as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)


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
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]

        for r in range(R):
            row = grid[r]
            for c in range(C):
                if row[c] != '@':
                    continue            # not a roll of paper

                cnt = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == '@':
                            cnt += 1
                if cnt < 4:
                    answer += 1
        return answer
    

    result_part1 = solve(input_lines)
    # ic(result_part1)

    tm_end = time.time()
    print(f"DEBUG: solve_part1 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part1 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part1 Delta: {tm_end-tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    tm_start = time.time()
    result_part2 = 0

    ic("DEBUG: TODO solve_part2()")

    tm_end = time.time()
    print(f"DEBUG: solve_part2 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part2 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part2 Delta: {tm_end-tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part2 result: {result_part2}")
    return result_part2


if __name__ == "__main__":
    solve_part1()
    # check_valid_id_part2("1010")
    # check_valid_id_part2("1011")
    solve_part2()
    pass

# EOF
