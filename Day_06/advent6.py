from collections import Counter

xfile = open("puzzle.txt")
xread = xfile.read()

# now works without adding a line at the end
# fuck knows why

l = xread.split("\n\n")
s = ([])

print("Solution 1:")

# looking for questions answered, so individual letters in each group
# add letters from each group to a set to get rid of duplicates
# count length of set to find out number of individual questions answered

a = 0

for i in l:
    cleani = i.replace("\n", "")
    s = {x for x in cleani}
    a += len(s)

print(a)

print("Solution 2:")

# use Counter to figure out how many people answered each question per group
# split group into persons by splitting at new line, use length of new group to find out number of people
# add all letters to set to get rid of duplicates
# for each letter in set, check how many people answered
# if number of people in group == number of people that answered question: success!

a = 0

for i in l:
    cleani = i.replace("\n", "")
    cnt = Counter(cleani)
    newl = i.split("\n")
    s = {x for x in cleani}
    for i in s:
        if cnt[i] == len(newl):
            a +=1

print(a)
