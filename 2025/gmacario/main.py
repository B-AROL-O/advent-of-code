# file: advent-of-code/2025/gmacario/main.py

import day01.solve_day01
import day02.solve_day02

def solve_challenge(day: int) -> bool:
    assert 1 <= day <= 12

    if day == 1:
        day01.solve_day01.solve_daily_challenge(day)
        print()
    elif day == 2:
        input_lines = day02.solve_day02.load_input()
        day02.solve_day02.solve_part1(input_lines)
        day02.solve_day02.solve_part2(input_lines)
        print()
    else:
        print(f"TODO: solve_challenge(day={day})")
        return False
    
    return True


def main():
    print("INFO:  Advent of Code 2025 solutions by gmacario")

    for day in range(1,13):
        solve_challenge(day)

if __name__ == "__main__":
    main()
