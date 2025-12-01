def read_file_lines(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f]


lines = read_file_lines("input.txt")

sum = 50
cntSumZero = 0
for line in lines:
    if line[0] == 'L':
        # print(str(sum) + " - " + l[1:], end="")
        sum -= int(line[1:])
    else:
        # print(str(sum) + " + " + l[1:], end="")
        sum += int(line[1:])
    sum %= 100
    # print(" = " + str(sum))
    if sum == 0:
        cntSumZero += 1

print("Solution part 1: " + str(cntSumZero))

sum = 50
cntSumZero = 0
for line in lines:
    n = int(line[1:])
    clicks = int(n / 100)
    mod = n % 100
    prev_sum = sum

    if line[0] == 'R':
        # print(str(sum) + " + " + line[1:], end="")
        sum += mod
    else:
        # print(str(sum) + " - " + line[1:], end="")
        sum -= mod

    if mod > 0:
        if sum == 0:
            clicks += 1
        else:
            if sum != (sum % 100):
                sum %= 100
                if prev_sum != 0:
                    clicks += 1
    cntSumZero += clicks
    # print(" = " + str(sum) + " | " + str(clicks))

print("Solution part 2: " + str(cntSumZero))
