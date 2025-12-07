import math


def read_file_lines(filename):
    with open(filename, 'r') as f:
        split_lines = [line.replace(
            "  ", " ").strip().split(" ") for line in f]
        return [[y for y in x if y.strip()] for x in split_lines]


def part1():
    grid = read_file_lines("input.txt")
    # print(grid)
    rows, cols = len(grid), len(grid[0])
    tot = 0
    for c in range(cols):
        op = grid[rows-1][c]
        col_tot = 0 if op == '+' else 1
        for r in range(rows-1):
            if op == '+':
                col_tot += int(grid[r][c])
            else:
                col_tot *= int(grid[r][c])
        # print(col_tot)
        tot += col_tot

    print("Solution part 1: ", tot)


def part2():
    grid = []
    with open('input.txt', 'r') as f:
        grid = [[c for c in x.strip('\n')] for x in f]

    ops = [x for x in grid[-1] if x.strip()]
    grid = grid[:-1]
    # print(grid, ops)
    rows, cols = len(grid), len(grid[0])
    operands = []
    tot = 0
    cur_op_idx = 0
    for c in range(cols):
        num = 0
        for r in range(rows):
            if grid[r][c] != ' ':
                num = num*10 + int(grid[r][c])
            elif num != 0:
                break

        # print(num)
        if num == 0:
            # empty column
            if ops[cur_op_idx] == '+':
                tot += sum(operands)
            else:
                tot += math.prod(operands)
            # sum to sum
            operands = []
            cur_op_idx += 1
        else:
            operands.append(num)
    if ops[cur_op_idx] == '+':
        tot += sum(operands)
    else:
        tot += math.prod(operands)

    print("Solution part 2: ", tot)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
