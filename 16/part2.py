filename = 'input.txt'


class Rule:

    def __init__(self, name, range1, range2):
        self.name = name
        self.range1 = range1
        self.range2 = range2

    def satisfy(self, no):
        if self.range1[0] <= no <= self.range1[1] or self.range2[0] <= no <= self.range2[1]:
            return True
        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


valid_lst = [False for i in range(1000)]

rule_lst = []

with open(filename) as file:
    for line in file:

        if line == '\n':
            break

        name = line.split(': ')[0]
        range1, range2 = line.strip().split(': ')[1].split(' or ')
        range1 = tuple(map(int, range1.split('-')))
        range2 = tuple(map(int, range2.split('-')))
        rule = Rule(name, range1, range2)
        rule_lst.append(rule)

        for start, end in [range1, range2]:
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
valid_ticket_id_lst = []
for i, ticket in enumerate(ticket_lst):
    for no in ticket:
        if not valid_lst[no]:
            break
    else:
        valid_ticket_id_lst.append(i)

ticket_lst = [ticket_lst[i] for i in valid_ticket_id_lst]

valid_lst = None

index2name = [None for _ in range(len(rule_lst))]

found_rule_lst = []

for _ in range(len(rule_lst)):
    for no_index in range(len(rule_lst)):
        valid_so_far = list(rule_lst)

        for rule in found_rule_lst:
            valid_so_far.remove(rule)

        for ticket in ticket_lst:
            no = ticket[no_index]

            temp = []
            for rule in valid_so_far:
                if rule.satisfy(no):
                    temp.append(rule)

            valid_so_far = temp

        if len(valid_so_far) == 1:
            rule = valid_so_far[0]
            print('Found {}'.format(rule))
            index2name[no_index] = rule.name
            found_rule_lst.append(rule)
            break

print(index2name)

departure_rule_indices = [index for index, name in enumerate(index2name) if name.startswith('departure')]
print(departure_rule_indices)

answer = 1
for index in departure_rule_indices:
    answer *= my_ticket[index]
print(answer)
