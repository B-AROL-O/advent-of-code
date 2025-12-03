import time

from icecream import ic

print("https://adventofcode.com/2025/day/2")

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


# ic()

# Read the puzzle input into a list of strings, one per line
with open("day02/input_day02_gmacario.txt", 'r') as file:
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


def solve_part1():
    ic(time.ctime())
    sum_invalid_ids_part1 = 0
    for p in products_id_range:
        for id in range(p["from"], p["to"]+1):
            # ic(id)
            if not check_valid_id_part1(str(id)):
                sum_invalid_ids_part1 += id
    print(f"Day02 Part 1 result: {sum_invalid_ids_part1}")
    ic(time.ctime())


def solve_part2():
    ic(time.ctime())

    sum_invalid_ids_part2 = 0
    for p in products_id_range:
        for id in range(p["from"], p["to"]+1):
            # ic(id)
            if not check_valid_id_part2(str(id)):
                sum_invalid_ids_part2 += id
    print(f"Day02 Part 2 result: {sum_invalid_ids_part2}")

    ic(time.ctime())
    pass


if __name__ == "__main__":
    solve_part1()
    # check_valid_id_part2("1010")
    # check_valid_id_part2("1011")
    solve_part2()
    pass

# EOF
