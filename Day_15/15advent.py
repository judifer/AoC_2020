import sys

sys.setrecursionlimit(10 ** 8)
numbers = [6,3,15,13,1,0]

max = 2020

def findlast(x, n):
    for idx, val in reversed(list(enumerate(n[:(len(n) - 1)]))):
        if val == x:
            a = len(n) - (idx + 1)
            return a

def adder(n):
    if n[-1] in n[:(len(n) - 1)]:
        a = findlast(n[-1], n)
        n.append(a)
    elif n[-1] not in n[:(len(n) - 1)]:
        n.append(0)
    if len(n) == max:
        return n[-1]
    else:
        return adder(n)

print("Solution 1:", adder(numbers))

numspot = dict()
numbers = [6,3,15,13,1,0]

a = 0
while a < (len(numbers) - 1):
    numspot[numbers[a]] = a + 1
    a += 1

round = a + 1
max = 30000000

num = numbers[-1]

while round <= max:
    if round == max:
        print("Solution 2:", num)
        break
    elif round < max:
        a = numspot.get(num)
        if a == None:
            newnum = 0
        elif a != None:
            newnum = round - a
        numspot[num] = round
        round += 1
        num = newnum
