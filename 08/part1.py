filename = 'input.txt'

inst_lst = []

with open(filename) as file:
    for line in file:
        op, arg = line.strip().split()
        arg = int(arg)
        inst_lst.append((op, arg))

acc = 0
inf_loop = False
i = 0

visited_set = set()

while not inf_loop:
    op, arg = inst_lst[i]

    if i in visited_set:
        inf_loop = True
        break

    visited_set.add(i)

    if op == 'acc':
        acc += arg
    elif op == 'jmp':
        i += arg
        continue

    i += 1

print(acc)