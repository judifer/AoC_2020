l = [int(x) for x in open("puzzle.txt").readlines()]

additions = set()
parameter = 25
x = 0

def listicle(p, x, l, s):
    temp = set()
    for i in l[x : x + p + 1]:
        for j in l[x : x + p + 1]:
            if i == j:
                pass
            else:
                sup = i + j
                temp.add(sup)
    s = [x for x in temp]
    return s

print("Solution 1:")

while x < (len(l) - parameter - 1):
    number = l[x + parameter]
    additions = listicle(parameter, x, l, additions)
    if number not in additions:
        print("Uh oh!", number)
        break
    elif number in additions:
        x +=1


print("Solution 2:")

y = 0
newl = []
addie = 0
a = 0

while y < (len(l) - 1):
    newl = []
    addie = 0
    y = a
    if l[y] == number:
        continue
    elif l[y] != number:
        while addie < number:
            addie += l[y]
            newl.append(l[y])
            y += 1
        if addie == number:
            print("Eureka!", min(newl) + max(newl))
            break
        else:
            a += 1
