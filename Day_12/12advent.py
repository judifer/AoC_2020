directions = [x.strip() for x in open('puzzle.txt').readlines()]

def course(d):
    north = 0
    east = 0
    south = 0
    west = 0
    face = 'east'
    solution = 0
    for i in d:
        fc = i[0]
        dr = int(i[1:])
        if fc == 'F':
            if face == 'east':
                east += dr
                west -= dr
            elif face == 'south':
                south += dr
                north -= dr
            elif face == 'west':
                west += dr
                east -= dr
            elif face == 'north':
                north += dr
                south -= dr
        elif fc == 'N':
            north += dr
            south -= dr
        elif fc == 'S':
            south += dr
            north -= dr
        elif fc == 'E':
            east += dr
            west -= dr
        elif fc == 'W':
            west += dr
            east -= dr
        elif fc == 'L':
            if face == 'north':
                if i[1:] == '90':
                    face = 'west'
                elif i[1:] == '180':
                    face = 'south'
                elif i[1:] == '270':
                    face = 'east'
            elif face == 'east':
                if i[1:] == '90':
                    face = 'north'
                elif i[1:] == '180':
                    face = 'west'
                elif i[1:] == '270':
                    face = 'south'
            elif face == 'south':
                if i[1:] == '90':
                    face = 'east'
                elif i[1:] == '180':
                    face = 'north'
                elif i[1:] == '270':
                    face = 'west'
            elif face == 'west':
                if i[1:] == '90':
                    face = 'south'
                elif i[1:] == '180':
                    face = 'east'
                elif i[1:] == '270':
                    face = 'north'
        elif fc == 'R':
            if face == 'north':
                if i[1:] == '90':
                    face = 'east'
                elif i[1:] == '180':
                    face = 'south'
                elif i[1:] == '270':
                    face = 'west'
            elif face == 'east':
                if i[1:] == '90':
                    face = 'south'
                elif i[1:] == '180':
                    face = 'west'
                elif i[1:] == '270':
                    face = 'north'
            elif face == 'south':
                if i[1:] == '90':
                    face = 'west'
                elif i[1:] == '180':
                    face = 'north'
                elif i[1:] == '270':
                    face = 'east'
            elif face == 'west':
                if i[1:] == '90':
                    face = 'north'
                elif i[1:] == '180':
                    face = 'east'
                elif i[1:] == '270':
                    face = 'south'
    if north > 0:
        solution += north
    if east > 0:
        solution += east
    if south > 0:
        solution += south
    if west > 0:
        solution += south
    return solution

def wayfinder(d):
    ship = [0, 0, 0, 0]
    # north, east, south, west
    waypoint = [1, 10, -1, -10]
    north = 0
    east = 0
    south = 0
    west = 0
    solution = 0
    for i in d:
        relative = []
        fc = i[0]
        dr = int(i[1:])
        if fc == 'N':
            waypoint[0] += dr
            waypoint[2] -= dr
        elif fc == 'S':
            waypoint[2] += dr
            waypoint[0] -= dr
        elif fc == 'E':
            waypoint[1] += dr
            waypoint[3] -= dr
        elif fc == 'W':
            waypoint[3] += dr
            waypoint[1] -= dr
        elif fc == 'L':
            if dr == 270:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[3], ship [1] + relative[0], ship[2] + relative[1], ship[3] + relative[2]]
            elif dr == 180:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[2], ship [1] + relative[3], ship[2] + relative[0], ship[3] + relative[1]]
            elif dr == 90:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[1], ship [1] + relative[2], ship[2] + relative[3], ship[3] + relative[0]]
        elif fc == 'R':
            if dr == 270:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[1], ship [1] + relative[2], ship[2] + relative[3], ship[3] + relative[0]]
            elif dr == 180:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[2], ship [1] + relative[3], ship[2] + relative[0], ship[3] + relative[1]]
            elif dr == 90:
                relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
                waypoint = [ship[0] + relative[3], ship [1] + relative[0], ship[2] + relative[1], ship[3] + relative[2]]
        elif fc == 'F':
            relative = [waypoint[0] - ship[0], waypoint[1] - ship[1], waypoint[2] - ship[2], waypoint[3] - ship[3]]
            ship[0] += (relative[0] * dr)
            ship[1] += (relative[1] * dr)
            ship[2] += (relative[2] * dr)
            ship[3] += (relative[3] * dr)
            waypoint = [ship[0] + relative[0], ship[1] + relative[1], ship[2] + relative[2], ship[3] + relative[3]]
    for coord in ship:
        if coord > 0:
            solution += coord
    return solution

print("Solution 1:", course(directions))
print("Solution 2:", wayfinder(directions))
