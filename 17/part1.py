from itertools import product

def count_active(i, j, k):
    retval = 0
    for (di, dj, dk) in neighbor_lst:
        if M[i + di][j + dj][k + dk] == ACTIVE:
            retval += 1
    return retval


filename = 'input.txt'

INACTIVE = '.'
ACTIVE = '#'
N = 30

neighbor_lst = list(product((-1, 0, 1), repeat=3))
print(len(neighbor_lst))
neighbor_lst.remove((0, 0, 0))
print(len(neighbor_lst))

M = [[[INACTIVE for k in range(N)] for j in range(N)] for i in range(N)]

with open(filename) as file:
    for i, line in enumerate(file):
        l = len(line) - 1
        M[15][i + 10][10:10 + l] = list(line.strip())

temp = [[[INACTIVE for k in range(N)] for j in range(N)] for i in range(N)]
for round in range(6):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                active_count = count_active(i, j, k)
                if M[i][j][k] == ACTIVE:
                    # print(i, j, k, active_count)
                    if active_count == 2 or active_count == 3:
                        temp[i][j][k] = ACTIVE
                        # print('active to active')
                    else:
                        temp[i][j][k] = INACTIVE
                else:
                    if active_count == 3:
                        temp[i][j][k] = ACTIVE
                    else:
                        temp[i][j][k] = INACTIVE

    M, temp = temp, M

    print(' ==== ROUND {} ===='.format(round + 1))

    print(*M[13], sep='\n')
    print()
    print(*M[14], sep='\n')
    print()
    print(*M[15], sep='\n')
    print()
    print(*M[16], sep='\n')
    print()
    print(*M[17], sep='\n')



# def count all actives
answer = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if M[i][j][k] == ACTIVE:
                answer += 1

print(answer)