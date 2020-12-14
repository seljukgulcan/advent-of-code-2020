from itertools import chain, combinations


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


filename = 'input.txt'

mask = None
and_mask = None
or_mask = None
x_mask = []

mem = dict()

with open(filename) as file:
    for line in file:
        if line.startswith('mask'):
            mask = line.strip()[-36:]
            and_mask = ['0' if bit == 'X' else '1' for bit in mask]  # to wash out X's
            or_mask = ['1' if bit == '1' else '0' for bit in mask]

            x_mask = []
            for i, bit in enumerate(mask[::-1]):
                if bit == 'X':
                    x_mask.append(2 ** i)

            and_mask = int(''.join(and_mask), 2)
            or_mask = int(''.join(or_mask), 2)

        elif line.startswith('mem'):
            index, value = line.strip().split("] = ")
            index = int(index[4:])
            value = int(value)

            index = index & and_mask
            index = index | or_mask

            for add_lst in powerset(x_mask):
                mem[index + sum(add_lst)] = value
        else:
            raise ValueError('Unexpected command')

print(sum(mem.values()))