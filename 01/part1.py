

filename = 'input.txt'

with open(filename) as file:
    no_set = set(map(int, file))

for no in no_set:
    if (2020 - no) in no_set:
        answer = no * (2020 - no)

print(answer)
