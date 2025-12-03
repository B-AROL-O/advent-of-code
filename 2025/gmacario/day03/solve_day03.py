import time

# from icecream import ic

print()

CHALLENGE_DAY=3

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


# Credits: gpt-oss:120b running on openwebui.gmacario.it
#
# Prompt:
#   Write a program in Python to solve Part Two of the following challenge:
#   (paste the contents of https://adventofcode.com/2025/day/3)
# 
def max_k_subseq(s: str, k: int = 12) -> int:
    """
    Return the integer represented by the lexicographically largest
    subsequence of length k of the digit string s.
    """
    stack = []                         # will contain characters, not ints
    n = len(s)

    for i, c in enumerate(s):
        # While we can improve the prefix by discarding a smaller digit,
        # and we still have enough characters left to reach length k,
        # pop the stack.
        while (stack and stack[-1] < c and
               (len(stack) - 1) + (n - i) >= k):
            stack.pop()

        # If we still need more characters, push the current one.
        if len(stack) < k:
            stack.append(c)
        # else: we already have k characters – ignore the rest.

    # At this point len(stack) == k
    return int(''.join(stack))


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")
    for bank in input_lines:
        result_part1 += find_largest_joltage(bank)

    tm_end = time.time()
    print(f"DEBUG: solve_part1 Begin: {time.ctime(tm_start)}")
    print(f"DEBUG: solve_part1 End:   {time.ctime(tm_end)}")
    print(f"DEBUG: solve_part1 Delta: {tm_end-tm_start}")
    print(f"INFO:  Day{CHALLENGE_DAY:02} solve_part1 result: {result_part1}")
    return result_part1


def solve_part2():
    tm_start = time.time()
    result_part2 = 0

    # ic("DEBUG: TODO solve_part2()")
    line_count = 0
    for line in input_lines:
        line_count += 1
        # ic(line_count, len(line))
        res = max_k_subseq(line)
        # ic(f"max_k_subseq({line}) is {res}")
        result_part2 += res

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
