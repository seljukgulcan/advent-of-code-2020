filename = 'input.txt'

x = 0
y = 0

dir_lst = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dir_index = 0


with open(filename) as file:
    for line in file:
        op = line[0]
        arg = int(line.strip()[1:])

        if op == 'N':
            y += arg
        elif op == 'S':
            y -= arg
        elif op == 'E':
            x += arg
        elif op == 'W':
            x -= arg

        elif op == 'R':
            dindex = arg // 90
            dir_index = (dir_index + dindex) % 4
        elif op == 'L':
            dindex = arg // 90
            dir_index = (dir_index - dindex) % 4

        elif op == 'F':
            dx, dy = dir_lst[dir_index]
            x += dx * arg
            y += dy * arg

print(x, y)
print(abs(x) + abs(y))
