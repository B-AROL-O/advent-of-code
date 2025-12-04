from collections import defaultdict


def read_file_lines(filename):
    with open(filename, 'r') as f:
        return [list(x.strip()) for x in f]


def main():
    grid = read_file_lines("input.txt")

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, -1), (1, 1), (-1, -1), (-1, 1)]
    cnt = defaultdict(int)

    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                for d in dirs:
                    r, c = i+d[0], j+d[1]
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == '@':
                        cnt[(r, c)] += 1

    lessthanfour = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and cnt[(i, j)] >= 0 and cnt[(i, j)] < 4:
                lessthanfour += 1
                print('x', end="")
            else:
                print(grid[i][j], end="")
        print()
    print()

    print("Solution part 1: ", lessthanfour)


if __name__ == "__main__":
    main()
