filename = 'input.txt'

inst_lst = []

with open(filename) as file:
    for line in file:
        op, arg = line.strip().split()
        arg = int(arg)
        inst_lst.append((op, arg))

found = False

for j in range(len(inst_lst)):

    if inst_lst[j][0] == 'nop':
        inst_lst[j] = ('jmp', inst_lst[j][1])
    elif inst_lst[j][0] == 'jmp':
        inst_lst[j] = ('nop', inst_lst[j][1])

    acc = 0
    i = 0
    visited_set = set()

    while True:

        if i == len(inst_lst):
            found = True
            break

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

    if inst_lst[j][0] == 'nop':
        inst_lst[j] = ('jmp', inst_lst[j][1])
    elif inst_lst[j][0] == 'jmp':
        inst_lst[j] = ('nop', inst_lst[j][1])

    if found:
        print(i)
        print(acc)
        break
