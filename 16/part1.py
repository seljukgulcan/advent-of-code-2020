filename = 'input.txt'

valid_lst = [False for i in range(1000)]

with open(filename) as file:
    for line in file:

        if line == '\n':
            break

        range1, range2 = line.strip().split(': ')[1].split(' or ')

        for range_str in [range1, range2]:
            start, end = map(int, range_str.split('-'))
            for i in range(start, end + 1):
                valid_lst[i] = True

    file.readline()
    my_ticket = list(map(int, file.readline().strip().split(',')))

    file.readline()
    file.readline()

    ticket_lst = []
    for line in file:
        ticket = list(map(int, line.strip().split(',')))
        ticket_lst.append(ticket)


total = 0
for ticket in ticket_lst:
    for no in ticket:
        if not valid_lst[no]:
            total += no

print(total)
