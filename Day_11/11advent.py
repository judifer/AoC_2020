waitroom = [[x for x in i.strip()] for i in open('puzzle.txt').readlines()]

def neighbours(seatplan, row, column):
    occupied = 0

    if row -1 >= 0:
        if column -1 >= 0:
            if seatplan[row-1][column-1] == "#":
                occupied += 1
        if column +1 < len(seatplan[row]):
            if seatplan[row-1][column+1] == "#":
                occupied += 1
        if seatplan[row-1][column] == "#":
            occupied += 1

    if column -1 >= 0:
        if seatplan[row][column-1] == "#":
            occupied += 1
    if column + 1 < len(seatplan[row]):
        if seatplan[row][column + 1] == "#":
            occupied += 1

    if row + 1 < len(seatplan):
        if column - 1 >= 0:
            if seatplan[row + 1][column - 1] == "#":
                occupied += 1
        if column + 1 < len(seatplan[row+1]):
            if seatplan[row + 1][column+1] == "#":
                occupied += 1
        if seatplan[row + 1][column] == "#":
            occupied += 1
    return occupied

def rushhour (input):
	new = []
	oldplan = input[:]
	while oldplan != new:
		if len(new) != 0:
			oldplan = new[:]
		new = [["" for i in row] for row in input]
		for row in range(len(oldplan)):
			for column in range(len(oldplan[row])):
				if oldplan[row][column] == "L":
					if neighbours(oldplan, row, column) == 0:
						new[row][column] = "#"
					else:
						new[row][column] = "L"
				elif oldplan[row][column] == "#":
					if neighbours(oldplan, row, column) >= 4:
						new[row][column] = "L"
					else:
						new[row][column] = "#"
				else:
					new[row][column] = "."

	result = 0
	for row in new:
		result += row.count("#")
	return result

print("Solution 1:", rushhour(waitroom))

#####################

def visible(seatplan,row, column):
	occupied = 0

	for vis_col in range(1,row + 1):
		if seatplan[row-vis_col][column] == "#":
			occupied += 1
			break
		elif seatplan[row-vis_col][column] == "L":
			break

	for vis_col in range(row+1, len(seatplan)):
		if seatplan[vis_col][column] == "#":
			occupied += 1
			break
		elif seatplan[vis_col][column] == "L":
			break

	for vis_row in range(column+1,len(seatplan[row])):
		if seatplan[row][vis_row] == "#":
			occupied += 1
			break
		elif seatplan[row][vis_row] == "L":
			break

	for vis_row in range(1,column+1):
		if seatplan[row][column-vis_row] == "#":
			occupied += 1
			break
		elif seatplan[row][column-vis_row] == "L":
			break

	vis_row = column + 1
	for vis_col in range(1,row + 1):
		if vis_row < len(seatplan[row]):
			if seatplan[row - vis_col][vis_row] == "#":
				occupied += 1
				break
			elif seatplan[row - vis_col][vis_row] == "L":
				break
			vis_row += 1

	vis_row = column - 1
	for vis_col in range(1, row + 1):
		if vis_row >= 0:
			if seatplan[row - vis_col][vis_row] == "#":
				occupied += 1
				break
			elif seatplan[row - vis_col][vis_row] == "L":
				break
			vis_row -= 1

	vis_row = column + 1
	for vis_col in range(row + 1, len(seatplan)):
		if vis_row < len(seatplan[row]):
			if seatplan[vis_col][vis_row] == "#":
				occupied += 1
				break
			elif seatplan[vis_col][vis_row] == "L":
				break
			vis_row += 1

	vis_row = column - 1
	for vis_col in range(row + 1, len(seatplan)):
		if vis_row >= 0:
			if seatplan[vis_col][vis_row] == "#":
				occupied += 1
				break
			elif seatplan[vis_col][vis_row] == "L":
				break
			vis_row -= 1

	return occupied

def part2 (input):
	new = []
	oldplan = input[:]
	while oldplan != new:
		if len(new) != 0:
			oldplan = new[:]
		new = [["" for i in row] for row in input]
		for row in range(len(oldplan)):
			for column in range(len(oldplan[row])):
				if oldplan[row][column] == "L":
					if visible(oldplan, row, column) == 0:
						new[row][column] = "#"
					else:
						new[row][column] = "L"
				elif oldplan[row][column] == "#":
					if visible(oldplan, row, column) >= 5 :
						new[row][column] = "L"
					else:
						new[row][column] = "#"
				else:
					new[row][column] = "."
	result = 0
	for row in new:
		result += row.count("#")
	return result

print("Solution 2:", part2(waitroom))
