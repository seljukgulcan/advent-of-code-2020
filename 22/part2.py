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

decks2result = dict()  # tuple(tuple, tuple) -> bool


def game(p1_deck, p2_deck):

    history = set()

    while p1_deck and p2_deck:

        hands = (tuple(p1_deck), tuple(p2_deck))
        if hands in history:
            return True
        history.add(hands)

        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        p1_won = False

        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:

            decks = (tuple(p1_deck), tuple(p2_deck))
            if decks in decks2result:
                p1_won = decks2result[decks]
            else:
                p1_won = game(p1_deck[:p1_card], p2_deck[:p2_card])
                decks2result[decks] = p1_won
        else:
            if p1_card > p2_card:
                p1_won = True

        if p1_won:
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)

    if p1_deck:
        return True
    return False


p1_won = game(p1_deck, p2_deck)

if p1_won:
    n = len(p1_deck)
    score = 0
    while p1_deck:
        score += p1_deck.pop(0) * n
        n -= 1
else:
    n = len(p2_deck)
    score = 0
    while p2_deck:
        score += p2_deck.pop(0) * n
        n -= 1

print(score)
