xfile = open("puzzle.txt")
xread = xfile.readlines()
a = 0
x = 0
loopcatch = set()

print("Solution 1:")

while x < len(xread):
    if x in loopcatch:
        break
    else:
        loopcatch.add(x)
        command, val = xread[x].split(" ")
        val = int(val)
        if command == 'acc':
            a += val
            x += 1
        elif command == 'jmp':
            if val == 0:
                print("Uh oh!", x)
            x += val
        elif command == 'nop':
            x += 1
print(a)

print("Solution 2:")

x = 0
a = 0
newcatch = set()
for i in loopcatch:
    # print(i)
    a = 0
    x = 0
    newcatch = set()
    while x < (len(xread) - 1):
        if x in newcatch:
            break
        elif x == i:
            newcatch.add(x)
            command, val = xread[x].split(" ")
            val = int(val)
            if command == 'acc':
                a += val
                x +=1
            elif command == 'jmp':
                x +=1
            elif command == 'nop':
                x += val
        else:
            newcatch.add(x)
            command, val = xread[x].split(" ")
            val = int(val)
            if command == 'acc':
                a += val
                x += 1
            elif command == 'jmp':
                x += val
            elif command == 'nop':
                x += 1
    if x >= (len(xread) - 1):
        print(a)
        break
