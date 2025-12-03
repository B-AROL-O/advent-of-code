import time

# from icecream import ic

print()

CHALLENGE_DAY=1

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, 'r') as file:
    input_lines = [line.rstrip() for line in file]

# ic(input_lines)


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")

    pos = 50
    count_zero = 0

    for line in input_lines:
        # ic(f"Processing line={line}")
        if line[:1] == 'L':
            pos -= int(line[1:])
        elif line[:1] == 'R':
            pos += int(line[1:])
        else:
            print(f"ERROR: Incorrect line={line}")
        pos %= 100
        # ic(f"Processed {line} ==> new pos={pos}")
        if pos == 0:
            count_zero += 1
    result_part1 = count_zero

    tm_end = time.time()
    print(f"DEBUG: solve_part1 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part1 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part1 Delta: {tm_end-tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    tm_start = time.time()
    result_part2 = 0

    # ic("TODO solve_part2()")

    # @gmacario original code
    #
    # pos = 50
    # count_zero_end = 0
    # count_zero_while = 0
    #
    # # ic(pos, count_zero_end, count_zero_while)
    # for line in input_lines:
    #     ic(f"Processing line={line}")
    #     if line[:1] == 'L':
    #         pos -= int(line[1:])
    #     elif line[:1] == 'R':
    #         pos += int(line[1:])
    #     else:
    #         print(f"ERROR: Incorrect line={line}")
    #
    #     while (pos >= 100):
    #         ic(f"pos={pos} --> sub(100)")
    #         pos -= 100
    #         # if pos != 0:
    #         ic(f"pos={pos} --> increment count_zero_while")
    #         count_zero_while += 1
    #     while (pos < 0):
    #         ic(f"pos={pos} --> add(100)")
    #         pos += 100
    #         # if pos != 0:
    #         # ic(f"pos={pos} --> increment_count_zero_while")
    #         # count_zero_while += 1
    #
    #     ic(f"Processed {line} ==> new pos={pos}")
    #
    #     if pos == 0:
    #         ic(f"pos={pos} --> increment count_zero_end")
    #         count_zero_end += 1
    #
    # result_part2 = count_zero_end + count_zero_while

    # Credits:
    # https://github.com/B-AROL-O/advent-of-code/compare/main...aleche28/day01#diff-64297c31a60452d2e8ab9bfbf1339279bc6ae2b0b51bdf89c38fb2b9c0ca179e
    #
    sum = 50
    cntSumZero = 0
    for line in input_lines:
        n = int(line[1:])
        clicks = int(n / 100)
        mod = n % 100
        prev_sum = sum

        if line[0] == 'R':
            # print(str(sum) + " + " + line[1:], end="")
            sum += mod
        else:
            # print(str(sum) + " - " + line[1:], end="")
            sum -= mod

        if mod > 0:
            if sum == 0:
                clicks += 1
            else:
                if sum != (sum % 100):
                    sum %= 100
                    if prev_sum != 0:
                        clicks += 1
        cntSumZero += clicks
        # print(" = " + str(sum) + " | " + str(clicks))
    result_part2 = cntSumZero

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
