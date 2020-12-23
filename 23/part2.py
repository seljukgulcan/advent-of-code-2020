from collections import deque

class Cup:

    def __init__(self, no):
        self.no = no
        # self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.no + 1)

    def print_cycle(self):
        current = self
        while current.next is not self:
            print('{} -> '.format(current), end='')
            current = current.next
        print('{} -> {}'.format(current, self))

label = '418976235'

lst = [x - 1 for x in map(int, label)]
N = 1000000

# Build linked-list
prev = None
current = None
no2cup = dict()

for no in lst:
    cup = Cup(no)
    no2cup[no] = cup

    if prev is None:
        current = cup
    else:
        prev.next = cup

    prev = cup

for no in range(9, N):
    cup = Cup(no)
    no2cup[no] = cup

    prev.next = cup
    prev = cup

prev.next = current

# current.print_cycle()

move_count = 10000000
for i in range(move_count):

    if i % 1000000 == 0:
        print(i)

    three_cups = current.next

    three_cups_set = set()

    temp = three_cups
    for _ in range(3):
        three_cups_set.add(temp.no)
        temp = temp.next

    current.next = three_cups.next.next.next

    destination_no = (current.no - 1) % N
    while destination_no in three_cups_set:
        destination_no = (destination_no - 1) % N

    dest = no2cup[destination_no]

    temp = dest.next
    dest.next = three_cups
    three_cups.next.next.next = temp

    current = current.next

    # print(current)
    # current.print_cycle()

cup_1 = no2cup[0]
no1 = cup_1.next.no + 1
no2 = cup_1.next.next.no + 1

answer = no1 * no2
print(answer)