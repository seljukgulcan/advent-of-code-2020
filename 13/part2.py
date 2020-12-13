filename = 'input.txt'

time_lst = []
with open(filename) as file:
    ts = int(file.readline())
    for time in file.readline().strip().split(','):
        if time != 'x':
            time_lst.append(int(time))
        else:
            time_lst.append(None)

# Applying chinese remainder theorem

equation_lst = []  # n_i, b_i
N = 1
for i, time in enumerate(time_lst):

    if time is None:
        continue

    i = i % time
    equation_lst.append((time, -i % time))
    N *= time


sum = 0
for n, b in equation_lst:
    n_i = N // n
    n_i = n_i % n
    z_i = None
    for i in range(n):
        if n_i * i % n == 1:
            z_i = i
            break
    if z_i is None:
        raise ValueError('n: {} b: {}'.format(n, b))

    n_i = N // n
    sum += z_i * n_i * b

print(sum % N)
