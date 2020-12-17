import math
from itertools import product

with open('puzzle.txt') as f:
    intprog = [x.strip() for x in f.readlines()]

memory = dict()

def convert(x):
    x = f'{x:b}'
    return x

def compare(x, m):
    a = -1
    temp = []
    while a >= (0 - len(m)):
        if m[a] == 'X':
            if a >= (0 - len(x)):
                temp.append(x[a])
            else:
                temp.append('0')
        elif m[a] != 'X':
            temp.append(m[a])
        a -= 1
    temp = temp[::-1]
    x = ''.join(temp)
    x = int(x, 2)
    return x

def getmask(line):
    x, y = [x.strip() for x in line.split('=')]
    return y

def getmemval(line):
    x, y = [x.strip() for x in line.split('=')]
    x = x.replace('mem', '').replace('[', '').replace(']', '')
    x = int(x)
    y = int(y)
    return x, y

for i in intprog:
    if i.startswith('mask'):
        mask = getmask(i)
    elif i.startswith('mem'):
        mem, val = getmemval(i)
        bitval = convert(val)
        finval = compare(bitval, mask)
        memory[mem] = finval

solution = 0

vals = []

vals = memory.values()

for i in vals:
    solution += i

print("Solution 1:", solution)

memory = dict()

def getallmem(x, m):
    a = -1
    temp = []
    mlist = []
    exchange = []
    while a >= (0 - len(m)):
        if m[a] == 'X':
            temp.append('X')
        elif m[a] == '0':
            if a >= (0 - len(x)):
                temp.append(x[a])
            else:
                temp.append('0')
        elif m[a] == '1':
            temp.append('1')
        a -= 1
    temp = temp[::-1]
    copy = []
    count = 0
    for i in temp:
        if i == 'X':
            count += 1
    exchange = list(product([0, 1], repeat=count))
    for i in exchange:
        z = 0
        copy = []
        for j in temp:
            if j == 'X':
                c = j.replace('X', str(i[z]))
                copy.append(c)
                z += 1
            else:
                copy.append(j)
        d = ''.join(copy)
        d = int(d, 2)
        mlist.append(d)
    return mlist

allthemems = []

for i in intprog:
    if i.startswith('mask'):
        mask = getmask(i)
    elif i.startswith('mem'):
        mem, val = getmemval(i)
        binmem = convert(mem)
        allthemems = getallmem(binmem, mask)
        for i in allthemems:
            memory[i] = val

solution = 0
vals = []
vals = memory.values()

for i in vals:
    solution += i

print("Solution 2:", solution)
