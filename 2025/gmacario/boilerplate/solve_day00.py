import time

from icecream import ic

print()

CHALLENGE_DAY=0

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
# INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"URL: {CHALLENGE_URL}")


# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, 'r') as file:
    input_lines = [line.rstrip() for line in file]

ic(input_lines)


def solve_part1():
    ic(time.ctime())

    ic("TODO solve_part1()")
    result_part1 = 0   # TODO

    print(f"Day{CHALLENGE_DAY:02} Part 1 result: {result_part1}")
    
    ic(time.ctime())


def solve_part2():
    ic(time.ctime())

    ic("TODO solve_part2()")
    result_part2 = 0   # TODO

    print(f"Day{CHALLENGE_DAY:02} Part 2 result: {result_part2}")

    ic(time.ctime())
    pass


if __name__ == "__main__":
    solve_part1()
    # check_valid_id_part2("1010")
    # check_valid_id_part2("1011")
    solve_part2()
    pass

# EOF
