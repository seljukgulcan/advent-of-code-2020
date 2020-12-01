filename = 'input.txt'

with open(filename) as file:
    no_lst = list(map(int, file))

pair_dict = dict()

for i, x in enumerate(no_lst):
    for y in no_lst[i + 1:]:
        if x + y < 2020:
            pair_dict[x + y] = (x, y)

for x in no_lst:
    if 2020 - x in pair_dict:
        y, z = pair_dict[2020 - x]
        print(x, y, z)
        answer = x * y * z
        print(answer)
