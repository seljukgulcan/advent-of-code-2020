import re

filename = 'input.txt'

required_field_set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid(d):

    for field in required_field_set:
        if field not in d:
            return False

    byr = d['byr']
    if len(byr) != 4:
        return False

    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return  False

    iyr = d['iyr']
    if len(iyr) != 4:
        return False

    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = d['eyr']
    if len(eyr) != 4:
        return False

    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = d['hgt']

    if hgt[-2:] == 'cm':
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            return False

    elif hgt[-2:] == 'in':
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            return False

    else:
        return False

    hcl = d['hcl']

    hcl_valid = re.search('^#[0-9a-f]{6}$', hcl)
    if hcl_valid is None:
        return False

    ecl = d['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid = d['pid']
    pid_valid = re.search('^[0-9]{9}$', pid)
    if pid_valid is None:
        return False

    return True


valid_count = 0
d = dict()

with open(filename) as file:
    for line in file:
        if line == '\n':
            if is_valid(d):
                valid_count += 1
            d = dict()

        for field in line.strip().split():
            key, value = field.split(':')
            d[key] = value

    if is_valid(d):
        valid_count += 1

print(valid_count)
