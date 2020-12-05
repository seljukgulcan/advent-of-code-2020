filename = 'input.txt'

max_id = 0

with open(filename) as file:
    for line in file:

        row_info = line[:7]
        col_info = line[7:].strip()

        row_info = row_info.replace('F', '0')
        row_info = row_info.replace('B', '1')
        row = int(row_info, 2)

        col_info = col_info.replace('L', '0')
        col_info = col_info.replace('R', '1')
        col = int(col_info, 2)

        seat_id = row * 8 + col

        if seat_id > max_id:
            max_id = seat_id

print(max_id)
