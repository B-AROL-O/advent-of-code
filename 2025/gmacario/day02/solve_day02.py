import time

# from icecream import ic

CHALLENGE_DAY=2

CHALLENGE_URL=f"https://adventofcode.com/2025/day/{CHALLENGE_DAY}"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/sample_day{CHALLENGE_DAY:02}.txt"
INPUT_FILE=f"day{CHALLENGE_DAY:02}/input_day{CHALLENGE_DAY:02}.txt"

print(f"INFO:  Advent of Code 2025 - Day {CHALLENGE_DAY}")
print(f"INFO:  URL: {CHALLENGE_URL}")

# ic()

# Read the puzzle input into a list of strings, one per line
with open(INPUT_FILE, 'r') as file:
    input_lines = [line.rstrip() for line in file]

products_id_range = []
for p in input_lines[0].split(','):
    p_range = p.split('-')
    # ic(p_range)
    p_from = int(p_range[0])
    p_to = int(p_range[1])
    products_id_range.append({
        "from": p_from,
        "to": p_to
    })
    pass

# ic(products_id_range)


"""
Check if the ID is valid (Part One).
You can find the invalid IDs by looking for any ID
which is made only of some sequence of digits repeated twice
"""
def check_valid_id_part1(id: str) -> bool:
    # ic(f"check_valid_id_part1(id={id})")

    # Odd length is valid
    if len(id) % 2:
        return True
    
    half_length = len(id) // 2
    if id[0:half_length] == id[half_length:]:
        # ic(f"id {id} is invalid (0)")
        return False

    return True


"""
Check if the ID is valid (Part Two).
You can find the invalid IDs by looking for any ID
which is made only of some sequence of digits
repeated **at least** twice
"""
def check_valid_id_part2(id: str) -> bool:
    # ic(f"check_valid_id_part2(id={id})")

    for k in range(1, len(id) // 2 + 1):
        prefix = id[0:k]
        pos = k
        has_match = True
        while pos < len(id) and has_match:
            # ic(f"checking id={id}, k={k}, pos={pos}")
            if prefix == id[pos:pos+k]:
                # ic(f"id {id}: prefix {prefix} found at pos {pos}")
                has_match = True
            elif has_match:
                # ic(f"id {id}: prefix {prefix} does not match at pos {pos}")
                has_match = False
            pos += k
        if has_match:
            # ic(f"id {id} is invalid (2)")
            return False

    # ic(f"id {id} is valid (3)")
    return True


def solve_part1():
    tm_start = time.time()
    result_part1 = 0

    # ic("DEBUG: TODO solve_part1()")

    sum_invalid_ids_part1 = 0
    for p in products_id_range:
        for id in range(p["from"], p["to"]+1):
            # ic(id)
            if not check_valid_id_part1(str(id)):
                sum_invalid_ids_part1 += id
    result_part1 = sum_invalid_ids_part1

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

    sum_invalid_ids_part2 = 0
    for p in products_id_range:
        for id in range(p["from"], p["to"]+1):
            # ic(id)
            if not check_valid_id_part2(str(id)):
                sum_invalid_ids_part2 += id
    result_part2 = sum_invalid_ids_part2

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
