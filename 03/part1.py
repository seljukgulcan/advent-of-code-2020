def find_no_trees(drow, dcol):
    row = 0
    col = 0

    retval = 0

    for _ in range(row_count):

        if grid[row][col % col_count] == '#':
            retval += 1

        row += drow
        col += dcol

    return retval


filename = 'input.txt'

with open(filename) as file:
    grid = list(map(list, file))

row_count = len(grid)
col_count = len(grid[0]) - 1

for i in range(row_count):
    grid[i].pop(-1)

print(row_count)
print(col_count)

answer = find_no_trees(1, 3)
print(answer)

