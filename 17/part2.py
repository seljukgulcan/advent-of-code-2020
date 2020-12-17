from itertools import product

def count_active(i, j, k, t):
    retval = 0
    for (di, dj, dk, dt) in neighbor_lst:
        if M[i + di][j + dj][k + dk][t + dt] == ACTIVE:
            retval += 1
    return retval


filename = 'input.txt'

INACTIVE = '.'
ACTIVE = '#'
N = 24

neighbor_lst = list(product((-1, 0, 1), repeat=4))
print(len(neighbor_lst))
neighbor_lst.remove((0, 0, 0, 0))
print(len(neighbor_lst))

M = [[[[INACTIVE for t in range(N)] for k in range(N)] for j in range(N)] for i in range(N)]

with open(filename) as file:
    for i, line in enumerate(file):
        l = len(line) - 1
        M[12][12][i + 8][8:8 + l] = list(line.strip())

temp = [[[[INACTIVE for t in range(N)] for k in range(N)] for j in range(N)] for i in range(N)]
for round in range(6):
    print(round)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                for t in range(1, N - 1):
                    active_count = count_active(i, j, k, t)
                    if M[i][j][k][t] == ACTIVE:
                        if active_count == 2 or active_count == 3:
                            temp[i][j][k][t] = ACTIVE
                        else:
                            temp[i][j][k][t] = INACTIVE
                    else:
                        if active_count == 3:
                            temp[i][j][k][t] = ACTIVE
                        else:
                            temp[i][j][k][t] = INACTIVE

    M, temp = temp, M


# def count all actives
answer = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for t in range(N):
                if M[i][j][k][t] == ACTIVE:
                    answer += 1

print(answer)