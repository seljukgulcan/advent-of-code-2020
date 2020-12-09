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
        invalid_no = no
        break

print(invalid_no)

for start in range(len(no_lst)):

    found = False

    total = no_lst[start]
    for end in range(start + 1, len(no_lst)):
        total += no_lst[end]

        if total == invalid_no:
            answer_lst = no_lst[start: end + 1]
            print(start, end)
            print(start + end)
            found = True
            break

    if found:
        break

print(min(answer_lst) + max(answer_lst))
