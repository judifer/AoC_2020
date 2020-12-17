# import time

# several different solutions all in one

xfile = open("puzzle.txt")
xread = xfile.readlines()

l = []

print("Problem 1:")

# start = time.time()
# each line of our input is a boarding pass
# each boarding pass has 10 letters
# [0:7] describes the row, [7:] describes the column
# F means it's in the first half of your current range of rows
# B means it's in the last half of your current range of rows
# L means it's in the first half of your current range of columns
# R means it's in the last half of your current range of columns
# Find out seat ID (8 * row + column)
# Find the highest seat ID!

x = 0
y = 127
a = 0
b = 7

for line in xread:
    if line[0] == "F":
        x = 0
        y = 63
    else:
        x = 64
        y = 127
    if line[1] == "F":
        y = y - 32
    else:
        x = x + 32
    if line[2] == "F":
        y = y - 16
    else:
        x = x + 16
    if line[3] == "F":
        y = y - 8
    else:
        x = x + 8
    if line[4] == "F":
        y = y - 4
    else:
        x = x + 4
    if line[5] == "F":
        y = y - 2
    else:
        x = x + 2
    if line[6] == "F":
        y = y - 1
    else:
        x = x + 1
    if line[7] == "L":
        a = 0
        b = 3
    else:
        a = 4
        b = 7
    if line[8] == "L":
        b = b - 2
    else:
        a = a + 2
    if line[9] == "L":
        b = b - 1
    else:
        a = a + 1
    seatid = x * 8 + a
    l.append(seatid)

l.sort()
print("Highest seat ID:", l[len(l) - 1])

# print("Time:", time.time() - start)

print("Problem 2:")

# start = time.time()

# the list of seat IDs we have should now have all boarding passes except for 1
# there are a few missing from the start but we don't care
# ours is in the middle, and the seat IDs before and after are present
# find our seat ID!

x = 0
y = x + 1
while x < (len(l) - 1):
    if (l[x] + 1) != l[y]:
        print("My seat ID:", l[x]+ 1)
        break
    x = x + 1
    y = y + 1

# print("Time:", time.time() - start)

print("Problem 1 but less hardcoded:")

# start = time.time()

l = []

for bigline in xread:
    line = bigline.strip()
    x = 0
    y = 127
    a = 0
    b = 7
    z = 64
    c = 4
    for i in line:
        if i == "F":
            y -= z
            z = z / 2
        elif i == "B":
            x += z
            z = z / 2
        elif i == "L":
            b -= c
            c = c / 2
        elif i == "R":
            a += c
            c = c / 2
        else:
            print("Something went wrong.")
    seatid = int(8 * x + a)
    l.append(seatid)

print("Highest seat ID:", max(l))

# print("Time:", time.time() - start)

print("Problem 2 but with 100% fewer while loops:")

# start = time.time()

myseat = [seat for seat in range(min(l), max(l)) if seat not in l]

print("My seat ID:", myseat[0])

# print("Time:", time.time() - start)

print("Problem 1 but also works with different number of rows/columns maybe?:")

# start = time.time()

def howmanyrows(x):
    count = 0
    for i in x:
        if (i == "F") or (i == "B"):
            count += 1
    return (2 ** count)

def howmanycolumns(x):
    count = 0
    for i in x:
        if (i == "L") or (i == "R"):
            count += 1
    return (2 ** count)

l = []

for bigline in xread:
    line = bigline.strip()
    firstrow = 0
    lastrow = howmanyrows(line) - 1
    rnumbers = howmanyrows(line) / 2
    firstcolumn = 0
    lastcolumn = howmanycolumns(line) -1
    cnumbers = howmanycolumns(line) / 2
    for i in line:
        if i == "F":
            lastrow -= rnumbers
            rnumbers /= 2
        elif i == "B":
            firstrow += rnumbers
            rnumbers /= 2
        elif i == "L":
            lastcolumn -= cnumbers
            cnumbers /= 2
        elif i == "R":
            firstcolumn += cnumbers
            cnumbers /= 2
    l.append(int(firstrow * 8 + firstcolumn))

print("The highest seat ID is:", max(l))

# print("Time:", time.time() - start)
