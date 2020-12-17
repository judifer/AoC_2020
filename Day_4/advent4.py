xfile = open("puzzle.txt")
xread = xfile.read()

passport = xread.split("\n\n")

count = 0
valid = 0

requirements = {'byr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid', 'eyr'}

for i in passport:
    line = i.replace("\n", " ")
    kv = line.split(' ')

    small_dictionary = {}
    for l in kv:
        k, v = l.split(':')
        small_dictionary[k] = v

    invalid = False
    for r in requirements:
        if r in small_dictionary:
            pass
        else:
            invalid = True
            break

    if invalid:
        continue

    for k,v in small_dictionary.items():
        if k == 'byr':
            if len(v) != 4:
                invalid = True
            else:
                if (int(v) < 1920) or (int(v) > 2002):
                    invalid = True

        elif k == 'hgt':
            if 'in' in v:
                vv = v.replace("in", "")
                if (int(vv) < 59) or (int(vv) > 76):
                    invalid = True
            elif 'cm' in v:
                vv = v.replace('cm', '')
                if (int(vv) < 150) or (int(vv) > 193):
                    invalid = True
            else:
                invalid = True

        elif k == "iyr":
            if len(v) != 4:
                invalid = True
            else:
                if (int(v) < 2010) or (int(v) > 2020):
                    invalid = True

        elif k == "eyr":
            if len(v) != 4:
                invalid = True
            else:
                if (int(v) < 2020) or (int(v) > 2030):
                    invalid = True

        elif k == "hcl":
            if len(v) != 7:
                invalid = True
            else:
                if v[0] != '#':
                    invalid = True
                else:
                    for m in v[1:]:
                        char_range = [str(x) for x in range(0, 9 + 1)]
                        char_range.extend([str(chr(x)) for x in range(ord('a'), ord('f') + 1)])
                        if m not in char_range:
                            invalid = True
                            break
        elif k == "ecl":
            if (v != "amb") and (v != "blu") and (v != "brn") and (v != "gry") and (v != "grn") and (v != "hzl") and (v != "oth"):
                invalid = True

        elif k == "pid":
            if len(v) != 9:
                invalid = True
            else:
                for m in v:
                    if int(m) not in range(0, 9 + 1):
                        invalid = True
                        break

        elif k == "cid":
            pass

        else:
            invalid = True

        if invalid:
            break

    if not invalid:
        count += 1

print(count)
