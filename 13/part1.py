import sys

filename = 'input.txt'

time_lst = []
with open(filename) as file:
    ts = int(file.readline())
    for time in file.readline().strip().split(','):
        if time != 'x':
            time_lst.append(int(time))

min_id = None
min_time = float('inf')

for time in time_lst:
    missed_interval = ts % time
    if missed_interval == 0:
        print(time)
        sys.exit(0)

    catch_time = ts - missed_interval + time

    if catch_time < min_time:
        min_time = catch_time
        min_id = time

wait_time = min_time - ts
print(min_id, min_time)
print(min_id * wait_time)
