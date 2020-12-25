filename = 'input.txt'

M = 20201227

with open(filename) as file:
    a, b = map(int, file.read().strip().split())

a_loopsize = None
b_loopsize = None

prev = 1
for i in range(1, 100_000_000):
    public = (prev * 7) % M

    if public == a:
        a_loopsize = i
    if public == b:
        b_loopsize = i

    if a_loopsize is not None and b_loopsize is not None:
        break

    prev = public
else:
    raise AssertionError('Couldnt found loop sizes')

pkey = 1
for _ in range(b_loopsize):
    pkey = (pkey * a) % M

print(pkey)
