from collections import Counter

xfile = open("puzzle.txt")
l = [int(x) for x in xfile.readlines()]
l.append((max(l) + 3))

x = 0
one_counter = 0
three_counter = 0

print("Solution 1:")

while x < max(l):
    if x + 1 in l:
        one_counter += 1
        x += 1
    elif x + 2 in l:
        x += 2
    elif x + 3 in l:
        three_counter += 1
        x += 3
    else:
        print("Uh oh!")
        print(x)
        break

result = one_counter * three_counter
print(result)

print("Solution 2:")

l.sort()
