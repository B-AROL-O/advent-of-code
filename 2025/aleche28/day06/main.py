
def read_file_lines(filename):
    with open(filename, 'r') as f:
        split_lines = [line.replace(
            "  ", " ").strip().split(" ") for line in f]
        return [[y for y in x if y.strip()] for x in split_lines]


def main():
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


if __name__ == "__main__":
    main()
