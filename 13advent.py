from sympy.ntheory.modular import crt

xfile = open('puzzle.txt')
xread = xfile.readlines()
time = xread[0].strip()
time = int(time)
busses = [int(x) for x in xread[1].replace('x,', '').split(',')]

waittime = 100

for bus in busses:
    x = time % bus
    wait = bus - x
    if wait < waittime:
        waittime = wait
        solution = waittime * bus

print("Solution 1:", solution)

busses = [x for x in xread[1].split(',')]
# print (busses)

busnum = []
rem = []
for t, bus in enumerate(busses):
    if bus != 'x':
        bus = int(bus)
        busnum.append(bus)
        rem.append(bus - t)

print("Solution 2:", crt(busnum, rem)[0])
