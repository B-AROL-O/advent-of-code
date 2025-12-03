import time

from icecream import ic

print()

CHALLENGE_DAY=0

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
# INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")

ic()

# Read the puzzle input into a list of strings, one per line
# with open(INPUT_FILE, 'r') as file:
#     input_lines = [line.rstrip() for line in file]

# ic(input_lines)


def solve_part1():
    print(f"DEBUG: solve_part1 Begin: {time.ctime()}")

    print("DEBUG: TODO solve_part1()")
    result_part1 = 0   # TODO

    print(f"DEBUG: solve_part1 End:   {time.ctime()}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    print(f"DEBUG: solve_part1 Begin: {time.ctime()}")

    print("DEBUG: TODO solve_part2()")
    result_part2 = 0   # TODO

    print(f"DEBUG: solve_part1 End:   {time.ctime()}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part2 result: {result_part2}")
    return result_part2


if __name__ == "__main__":
    solve_part1()
    # check_valid_id_part2("1010")
    # check_valid_id_part2("1011")
    solve_part2()
    pass

# EOF
