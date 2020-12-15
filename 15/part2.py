filename = 'input.txt'

lst = [0, 12, 6, 13, 20, 1]
# lst = [0, 3]

no2turn = {no: i + 1 for i, no in enumerate(lst)}

last_no = 17
# last_no = 6

for i in range(len(lst) + 1, 30000000):

    answer = None

    if last_no in no2turn:
        age = i - no2turn[last_no]
        answer = age
    else:
        answer = 0

    no2turn[last_no] = i

    last_no = answer

print(last_no)
