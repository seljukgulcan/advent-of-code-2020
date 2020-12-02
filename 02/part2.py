from collections import Counter

filename = 'input.txt'

valid_count = 0

with open(filename) as file:
    for line in file:
        policy, password = line.split(':')
        counts, letter = policy.split()
        min, max = map(int, counts.split('-'))
        password = password.strip()

        first_matched = password[min - 1] == letter
        second_matched = password[max - 1] == letter

        if first_matched != second_matched:
            valid_count += 1

print(valid_count)
