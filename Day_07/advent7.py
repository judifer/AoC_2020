

xfile = open('puzzle.txt')
xread = xfile.readlines()

bagdict = {}
layerbags = set()

for i in xread:
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    p1, p2 = i.replace('bags', '').replace('bag', '').split('contain')
    p1 = p1.strip().replace('.', '')
    p2 = p2.strip().replace('.', '')
    if ',' in p2:
        p2 = p2.split(', ')
        p2 = [x.strip() for x in p2]
        bagdict[p1] = p2
    else:
        bagdict[p1] = [p2]

    for i in bagdict:
        if 'shiny gold' in p2:
            layerbags.add(p1)
        else:
            for j in p2:
                if 'shiny gold' in j:
                    layerbags.add(p1)

# print(layerbags)
# print(bagdict)
# # print(bagdict)

print('Solution 1:')

while True:
    temp = set()
    for i in layerbags:
        for key, value in bagdict.items():
            for child in value:
                # print(i, key, child)
                if i in child:
                    if key not in layerbags:
                        temp.add(key)

    if len(temp) == 0:
        break
    else:
        # print(temp)
        layerbags = layerbags | temp


print(len(layerbags))
# print(layerbags)

print('Solution 2:')

solution_list = set()
