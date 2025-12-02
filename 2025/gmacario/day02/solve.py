# https://adventofcode.com/2025/day/2

import time

from icecream import ic

"""
Check if the ID is valid.
You can find the invalid IDs by looking for any ID
which is made only of some sequence of digits repeated twice
"""
def check_valid_id(id: str) -> bool:
    # ic(f"check_valid_id(id={id})")

    # Odd length is valid
    if len(id) % 2:
        return True
    
    half_length = len(id) // 2
    if id[0:half_length] == id[half_length:]:
        ic(f"id {id} is invalid")
        return False

    return True


ic()

# Read the puzzle input into a list of strings, one per line
with open("day02/input_day02_gmacario.txt", 'r') as file:
    input_lines = [line.rstrip() for line in file]

ic(time.ctime())

ic(input_lines)

products = input_lines[0].split(',')
ic(products)

sum_invalid_ids = 0
for p in products:
    ic(p)
    p_range = p.split('-')
    # ic(p_range)
    p_from = int(p_range[0])
    p_to = int(p_range[1])
    ic(p_from, p_to)

    for id in range(p_from, p_to+1):
        # ic(id)
        if not check_valid_id(str(id)):
            sum_invalid_ids += id

ic(sum_invalid_ids)

ic(time.ctime())

# EOF
