def find_no_trees(drow, dcol):
    row = 0
    col = 0

    retval = 0

    while True:

        if grid[row][col % col_count] == '#':
            retval += 1

        row += drow
        col += dcol

        if row >= row_count:
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

'''
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''

slope_lst = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

answer = 1
for slope in slope_lst:
    answer = answer * find_no_trees(*slope)
print(answer)

