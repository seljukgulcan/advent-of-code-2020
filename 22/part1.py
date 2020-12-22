from collections import deque

filename = 'input.txt'

p1_deck = []
p2_deck = []

with open(filename) as file:
    file.readline()
    for line in file:
        if line == '\n':
            break
        p1_deck.append(int(line))

    file.readline()
    for line in file:
        if line == '\n':
            break
        p2_deck.append(int(line))

print(p1_deck)

p1_deck = deque(p1_deck)
p2_deck = deque(p2_deck)

while p1_deck and p2_deck:
    p1_card = p1_deck.popleft()
    p2_card = p2_deck.popleft()

    if p1_card > p2_card:
        p1_deck.append(p1_card)
        p1_deck.append(p2_card)
    elif p2_card > p1_card:
        p2_deck.append(p2_card)
        p2_deck.append(p1_card)
    else:
        raise ValueError

if p1_deck:
    n = len(p1_deck)
    score = 0
    while p1_deck:
        score += p1_deck.popleft() * n
        n -= 1
else:
    print(p2_deck)
    n = len(p2_deck)
    score = 0
    while p2_deck:
        score += p2_deck.popleft() * n
        n -= 1

print(score)