from pprint import pprint
xfile = open("puzzle.txt")
lines = xfile.readlines()

total = 0

def trees(x_step, y_step):
    y = 0
    x = 0
    count = 0
    while y < len(lines):
        currentline = lines[y].strip()
        if currentline[x] == '#':
            count += 1
        y += y_step
        x = (x + x_step) % len(currentline)
    return count

total = trees(3, 1)
total *= trees(1, 1)
total *= trees(5, 1)
total *= trees(7, 1)
total *= trees(1, 2)
print(total)


grid = []

for y in range(10):
    grid.append([])
    for x in range(10):
        if x % 2:
            grid[y].append('1')
        else:
            grid[y].append('0')





pprint(grid)


 def trees(x, y):
     currentline = lines[x]
     print(currentline)
     #    ...##.###..###


     if currentline[(x * 3) % 32] == "#":
         y += 1

     for i in currentline:
         #.
         #.


         if i[(x * 3) % 32] == "#":
             y += 1
     x += 1
     if x == 1:
         return bla
     else:
         return trees(x, y)


 trees(pos, count)
 print(count)
