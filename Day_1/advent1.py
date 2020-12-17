xfile = open("puzzle.txt")
xread = [int(x) for x in xfile.readlines()]

holder = {}
for item in xread:
    if item in holder:
        print("Solution 1:", item * holder[item])
    else:
        inverse = 2020 - item
        holder[inverse] = item


def problem2(xread):
    for item in xread:
        for another in xread:
            for more in xread:
                if item == another or item == more and another == more:
                    continue
                if item + another + more == 2020:
                    return item * another * more

print("Solution 2:", problem2(xread))
