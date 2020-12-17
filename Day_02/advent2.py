xfile = open("puzzle.txt")
xlines = xfile.readlines()

countright = 0

for i in xlines:
    count = 0
    a, b, c = i.split()
    d, e = a.split("-")
    letter = b[0]
    pos1 = int(d) - 1
    pos2 = int(e) - 1
    if c[pos1] == letter:
        if c[pos2] != letter:
            countright = countright + 1
    elif c[pos2] == letter:
        if c[pos1] != letter:
            countright = countright + 1

print(countright)
