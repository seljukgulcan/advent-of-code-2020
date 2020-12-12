filename = 'input.txt'

x = 0
y = 0

dir_lst = [(1, 0), (0, -1), (-1, 0), (0, 1)]

wp = [10, 1]


def rotate(dir, angle):
    angle = angle // 90
    if dir == 'L':
        angle = 4 - angle

    if angle == 1:
        wp[0], wp[1] = wp[1], -wp[0]
    elif angle == 2:
        wp[0], wp[1] = -wp[0], -wp[1]
    elif angle == 3:
        wp[0], wp[1] = -wp[1], wp[0]
    else:
        raise ValueError('Unexpected rotation')


with open(filename) as file:
    for line in file:
        op = line[0]
        arg = int(line.strip()[1:])

        if op == 'N':
            wp[1] += arg
        elif op == 'S':
            wp[1] -= arg
        elif op == 'E':
            wp[0] += arg
        elif op == 'W':
            wp[0] -= arg

        elif op == 'R':
            rotate(op, arg)
        elif op == 'L':
            rotate(op, arg)

        elif op == 'F':
            x += wp[0] * arg
            y += wp[1] * arg

print(x, y)
print(abs(x) + abs(y))
