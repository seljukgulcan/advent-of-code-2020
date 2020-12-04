filename = 'input.txt'

required_field_set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_count = 0

field_set = set()

with open(filename) as file:
    for i, line in enumerate(file):
        if line == '\n':
            if required_field_set.issubset(field_set):
                valid_count += 1
            field_set = set()

        field_set = field_set.union(set(map(lambda x: x.split(':')[0], line.strip().split())))

    if required_field_set.issubset(field_set):
        valid_count += 1

print(valid_count)
