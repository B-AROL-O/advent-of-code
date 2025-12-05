
def read_file_lines(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f]


def main():
    ranges = []
    breakpoint = -1
    lines = read_file_lines("input.txt")
    for i, line in enumerate(lines):
        if not line:
            breakpoint = i
            break
        interval = tuple([int(x) for x in line.split('-')])
        ranges.append(interval)

    # double sort: apply sort by end number ascending and then by first number ascending
    ranges = sorted(ranges, key=lambda x: x[1])
    ranges = sorted(ranges, key=lambda x: x[0])
    # print(ranges)

    fresh = 0
    for i in range(breakpoint+1, len(lines)):
        el = int(lines[i])
        # a binary search would be better but i don't have time to write it
        for j in range(len(ranges)):
            if ranges[j][0] <= el and el <= ranges[j][1]:
                # print(el, " fresh; interval ", ranges[j][0], "-", ranges[j][1])
                fresh += 1
                break

    print("Solution part 1: ", fresh)

    # ranges are sorted by starting number ascending, ending number ascending
    untangledRanges = []
    curStart = ranges[0][0]
    curEnd = ranges[0][1]
    totSize = 0
    for i in range(1, len(ranges)):
        rng = ranges[i]
        if rng[0] <= curEnd:
            # overlapping
            # |---|
            #   |---|
            # becomes:
            # |-----|
            curEnd = max(curEnd, rng[1])
            # the following code is buggy because it shrinks when the interval is included
            # curEnd = rng[1]
        else:
            # not overlapping:
            # save current one and restart from new one
            untangledRanges.append((curStart, curEnd))
            totSize += (curEnd-curStart+1)
            curStart = rng[0]
            curEnd = rng[1]
    # last one:
    untangledRanges.append((curStart, curEnd))
    totSize += (curEnd-curStart+1)

    # print(untangledRanges)
    print("Solution part 2: ", totSize)


if __name__ == "__main__":
    main()
