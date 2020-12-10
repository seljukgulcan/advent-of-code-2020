filename = 'input.txt'

with open(filename) as file:
    jolt_lst = [int(line) for line in file]

jolt_lst.sort()
jolt_lst.append(jolt_lst[-1] + 3)
print(jolt_lst)

diff_count_1 = 0
diff_count_3 = 0

jolt_lst.insert(0, 0)

for i in range(len(jolt_lst) - 1):
    current_jolt = jolt_lst[i]
    next_jolt = jolt_lst[i + 1]

    diff = next_jolt - current_jolt
    if diff == 1:
        diff_count_1 += 1
    elif diff == 3:
        diff_count_3 += 1

answer = diff_count_1 * diff_count_3
print(diff_count_1, diff_count_3)
print(answer)