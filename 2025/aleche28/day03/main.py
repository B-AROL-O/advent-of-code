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


def max_subsequence_sum(v, req_len):
    if req_len > len(v):
        print(f"no subsequence of {req_len} is possible")
        return None

    maxes = {0: 0}

    for i in range(1, len(v)+1):
        el = int(v[-i])
        # print("element: ", el)
        for j in range(min(i, req_len), 0, -1):  # go backwards to avoid dirtying maxes
            if maxes[j-1]+el*10**(j-1) > maxes.get(j, 0):
                maxes[j] = maxes[j-1]+el*10**(j-1)
        # for k, val in maxes.items():
        #     print("  ", k, ": ", val)

    return maxes[req_len]


def main():
    lines = read_file_lines("input.txt")

    sum = 0
    for line in lines:
        max1, idx1 = find_max(line[:-1])
        max2, _ = find_max(line[idx1+1:])
        sum += max1*10 + max2

    print("Solution part 1: ", sum)

    # part 2:
    # the idea is to go from the last element of the array
    # and keep track of the highest sum of x elements until now
    # for example: [5,7,2,6]
    # array element -> (l,max) where l is the length of the subseq
    # and max is the max sum of subsequences of length l considered until now
    # at every step, iterating on the lengths from 1 to n, check if the sum of the current
    # element at index i plus the max sum of length i-1 is greater than the max sum of length i,
    # in that case update it.
    # 6 -> (1,6)
    # 2 -> (1,6);(2,8) - 8 obtained by sum of 6 (max sum of 1 element array) and 2 (current element)
    # 7 -> (1,7);(2,13);(3,15) - (2,8) becomes (2,13) because the 1-el max sum (6)
    #                             plus the current el (7) is higher than the old one (8).
    # 5 -> (1,7);(2,13);(3,18);(4,)

    sum = 0
    for line in lines:
        maxSubSum = max_subsequence_sum(line, 12)
        # print(maxSubSum)
        sum += maxSubSum
    print("Solution part 2: ", sum)


if __name__ == "__main__":
    main()
