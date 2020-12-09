filename = 'input.txt'

with open(filename) as file:
    no_lst = [int(line.strip()) for line in file]

for i, no in enumerate(no_lst[25:]):
    preamble = no_lst[i: i + 25]

    found = False
    for a in range(25):
        for b in range(25):
            if preamble[a] + preamble[b] == no:
                found = True
                break
        if found:
            break

    if not found:
        print(no)
