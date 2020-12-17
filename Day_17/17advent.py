from itertools import product


# print(coords)

def problem1():
    with open('puzzle.txt') as f:
        vladimir = f.readlines()

    coords = dict()

    for y, vlad in enumerate(vladimir):
        for x, imir in enumerate(vlad):
            if imir == '#':
                coords[(x, y, 0)] = 1
            else:
                coords[(x, y, 0)] = 0

    cycle = 0
    while cycle < 6:
        new_coords = dict(coords)
        x = [x for x, y, z in coords.keys()]
        y = [y for x, y, z in coords.keys()]
        z = [z for x, y, z in coords.keys()]
        minx, maxx = min(x), max(x) #hihi minx
        # print(minx, maxx)
        miny, maxy = min(y), max(y)
        minz, maxz = min(z), max(z) #hihi minz

        # neighbours = list(product([-1, 0, 1], repeat=27))
        # print(neighbours)
        # break

        for ox in range(minx - 1, maxx + 2):
            for oy in range(miny -1, maxy + 2):
                for oz in range(minz -1, maxz + 2):
                    cubes = 0
                    for x in range(ox - 1, ox + 2):
                        for y in range(oy - 1, oy + 2):
                            for z in range(oz - 1, oz + 2):
                                if x == ox and y == oy and z == oz:
                                    continue
                                onoff = (x, y, z)
                                a = coords.get(onoff, 0)
                                # print(a)
                                cubes += a
                    cpoint = (ox, oy, oz)
                    active = coords.get(cpoint, 0)
                    if active:
                        if (cubes == 2) or (cubes == 3):
                            new_coords[cpoint] = 1
                        else:
                            new_coords[cpoint] = 0
                    else:
                        if cubes == 3:
                            new_coords[cpoint] = 1
                        else:
                            new_coords[cpoint] = 0

        # print(coords)
        # print(new_coords)
        coords = new_coords
        cycle += 1

    return sum(coords.values())



print("Solution 1:", problem1())

def problem2():
    with open('puzzle.txt') as f:
        vladimir = f.readlines()

    coords = dict()

    for y, vlad in enumerate(vladimir):
        for x, imir in enumerate(vlad):
            if imir == '#':
                coords[(x, y, 0, 0)] = 1
            else:
                coords[(x, y, 0, 0)] = 0

    cycle = 0
    while cycle < 6:
        new_coords = dict(coords)
        x = [x for x, y, z, w in coords.keys()]
        y = [y for x, y, z, w in coords.keys()]
        z = [z for x, y, z, w in coords.keys()]
        w = [w for x, y, z, w in coords.keys()]

        minx, maxx = min(x), max(x) #hihi minx
        # print(minx, maxx)
        miny, maxy = min(y), max(y)
        minz, maxz = min(z), max(z) #hihi minz
        minw, maxw = min(w), max(w)

        # neighbours = list(product([-1, 0, 1], repeat=27))
        # print(neighbours)
        # break

        for ox in range(minx - 1, maxx + 2):
            for oy in range(miny -1, maxy + 2):
                for oz in range(minz -1, maxz + 2):
                    for ow in range(minw - 1, maxw + 2):
                        cubes = 0
                        for x in range(ox - 1, ox + 2):
                            for y in range(oy - 1, oy + 2):
                                for z in range(oz - 1, oz + 2):
                                    for w in range(ow -1, ow + 2):
                                        if x == ox and y == oy and z == oz and w == ow:
                                            continue
                                        onoff = (x, y, z, w)
                                        a = coords.get(onoff, 0)
                                        # print(a)
                                        cubes += a
                        cpoint = (ox, oy, oz, ow)
                        active = coords.get(cpoint, 0)
                        if active:
                            if (cubes == 2) or (cubes == 3):
                                new_coords[cpoint] = 1
                            else:
                                new_coords[cpoint] = 0
                        else:
                            if cubes == 3:
                                new_coords[cpoint] = 1
                            else:
                                new_coords[cpoint] = 0

        # print(coords)
        # print(new_coords)
        coords = new_coords
        cycle += 1

    return sum(coords.values())

print("Solution 2:", problem2())
