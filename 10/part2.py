filename = 'input.txt'

with open(filename) as file:
    jolt_lst = [int(line) for line in file]

jolt_lst.sort()
jolt_lst.append(jolt_lst[-1] + 3)
jolt_lst.insert(0, 0)

m = [0 for _ in range(len(jolt_lst))]
m[0] = 1

for i in range(1, len(jolt_lst)):

    if jolt_lst[i] - jolt_lst[i - 1] <= 3:
        m[i] = m[i - 1]
    if i >= 2 and jolt_lst[i] - jolt_lst[i - 2] <= 3:
        m[i] += m[i - 2]
    if i >= 3 and jolt_lst[i] - jolt_lst[i - 3] <= 3:
        m[i] += m[i - 3]

print(m[-1])
