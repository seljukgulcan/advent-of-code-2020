filename = 'input.txt'

mask = None
and_mask = None
or_mask = None

mem = dict()

with open(filename) as file:
    for line in file:
        if line.startswith('mask'):
            mask = line.strip()[-36:]
            and_mask = ['0' if bit == '0' else '1' for bit in mask]
            or_mask = ['1' if bit == '1' else '0' for bit in mask]

            and_mask = int(''.join(and_mask), 2)
            or_mask = int(''.join(or_mask), 2)

        elif line.startswith('mem'):
            index, value = line.strip().split("] = ")
            index = int(index[4:])
            value = int(value)

            value = value & and_mask
            value = value | or_mask
            mem[index] = value
        else:
            raise ValueError('Unexpected command')

print(sum(mem.values()))