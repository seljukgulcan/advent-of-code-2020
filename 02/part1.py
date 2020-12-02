from collections import Counter

filename = 'input.txt'

valid_count = 0

with open(filename) as file:
    for line in file:
        policy, password = line.split(':')
        counts, letter = policy.split()
        min, max = map(int, counts.split('-'))
        password = password.strip()

        letter2count = Counter(password)

        count = letter2count[letter]

        if min <= count <= max:
            valid_count += 1

print(valid_count)
