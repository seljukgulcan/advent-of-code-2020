filename = 'input.txt'

FLOOR = 2
EMPTY = 0
FULL = 1

dir_lst = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1), (0, 1),
           (1, -1), (1, 0), (1, 1)]


def process(M):
    change_count = 0
    new_M = [[None for j in range(col_count)] for i in range(row_count)]

    for i in range(row_count):
        for j in range(col_count):
            seat = M[i][j]

            if seat == FLOOR:
                new_M[i][j] = FLOOR

            elif seat == EMPTY:
                for drow, dcol in dir_lst:
                    nrow = i + drow
                    ncol = j + dcol

                    while 0 <= nrow < row_count and 0 <= ncol < col_count and M[nrow][ncol] == FLOOR:
                        nrow += drow
                        ncol += dcol

                    if 0 <= nrow < row_count and 0 <= ncol < col_count and M[nrow][ncol] == FULL:
                        new_M[i][j] = EMPTY
                        break
                else:
                    new_M[i][j] = FULL
                    change_count += 1

            elif seat == FULL:

                full_count = 0
                for drow, dcol in dir_lst:
                    nrow = i + drow
                    ncol = j + dcol

                    while 0 <= nrow < row_count and 0 <= ncol < col_count and M[nrow][ncol] == FLOOR:
                        nrow += drow
                        ncol += dcol

                    if 0 <= nrow < row_count and 0 <= ncol < col_count and M[nrow][ncol] == FULL:
                        full_count += 1

                if full_count >= 5:
                    new_M[i][j] = EMPTY
                    change_count += 1
                else:
                    new_M[i][j] = FULL

            else:
                raise ValueError('Unexpected seat value: {}'.format(M[i][j]))

    return new_M, change_count


with open(filename) as file:
    M = [list(map(int, line.strip().replace('.', '2')
                                   .replace('#', '1')
                                   .replace('L', '0'))) for line in file]

row_count = len(M)
col_count = len(M[0])

change_count = 1
while change_count > 0:
    M, change_count = process(M)

answer = 0
for row in range(row_count):
    for col in range(col_count):
        if M[row][col] == FULL:
            answer += 1
print(answer)
