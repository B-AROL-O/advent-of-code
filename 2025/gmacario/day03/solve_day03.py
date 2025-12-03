import time

from icecream import ic

print()

CHALLENGE_DAY=3

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
# INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")

def find_largest_joltage(bank: str) -> int:
    result = 0

    for k1 in range(len(bank) - 1):
        battery_1 = bank[k1]
        for k2 in range(k1+1, len(bank)):
            battery_2 = bank[k2]
            joltage = 10 * int(battery_1) + int(battery_2)
            if joltage > result:
                # ic(f"Got better joltage {joltage} from bank {bank}[{k1},{k2}]")
                result = joltage
    # ic(f"find_largest_joltage({bank}) return {result}")
    return result

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, 'r') as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)


def solve_part1():
    print(f"DEBUG: solve_part1 Begin: {time.ctime()}")

    # print("DEBUG: TODO solve_part1()")
    result_part1 = 0
    for bank in input_lines:
        result_part1 += find_largest_joltage(bank)

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
