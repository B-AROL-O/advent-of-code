def read_file_lines(filename):
    with open(filename, 'r') as f:
        return [list(x.strip()) for x in f]


def find_max(line):
    max = 0
    idx = -1
    for i, n in enumerate(line):
        if int(n) > max:
            max = int(n)
            idx = i
    return max, idx


def main():
    lines = read_file_lines("input.txt")

    sum = 0
    for line in lines:
        max1, idx1 = find_max(line[:-1])
        max2, _ = find_max(line[idx1+1:])
        sum += max1*10 + max2

    print("Solution part 1: ", sum)


if __name__ == "__main__":
    main()
