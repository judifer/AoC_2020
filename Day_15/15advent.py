import sys

sys.setrecursionlimit(10 ** 8)

numbers = [6,3,15,13,1,0]

def findlast(x, n):
    for idx, val in reversed(list(enumerate(n[:(len(n) - 1)]))):
        # print(idx, val)
        if val == x:
            a = len(n) - (idx + 1)
            return a

def adder(n):
    if n[-1] in n[:(len(n) - 1)]:
        a = findlast(n[-1], n)
        n.append(a)
    elif n[-1] not in n[:(len(n) - 1)]:
        n.append(0)
    if len(n) == 2020:
        return n[-1]
    else:
        return adder(n)

print("Solution 1:", adder(numbers))

numspot = dict()

numbers = [6,3,15,13,1,0]

a = 1
while a < (len(numbers)- 1):
    numspot[numbers[a]] = a
    a += 1

# print(a)
# print(numspot)

def part2(dick, round, num):
    round += 1
    newnum = dick.get(num)
    print(newnum)
    if newnum == None:
        dick[num] = round
        newnum = 0
    if round == 2020:
        return newnum
    else:
        return part2(dick, round, newnum)

print("Solution 2:", part2(numspot, a, numbers[-1]))


# print("Solution 2:", part2(numspot, a, numbers[-1]))
