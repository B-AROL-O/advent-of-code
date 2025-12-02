def read_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readline().strip().split(',')


def main():
    intervals = read_file_lines("input.txt")
    sum = 0
    for interval in intervals:
        a = int(interval.split('-')[0])
        b = int(interval.split('-')[1])
        print(a, b)
        for i in range(a, b+1):
            if len(str(i)) % 2 == 0:
                numstr = str(i)
                h = int(len(numstr) / 2)
                if numstr[:h] == numstr[h:]:
                    print("invalid: " + numstr)
                    sum += i
    print(sum)


if __name__ == "__main__":
    main()
