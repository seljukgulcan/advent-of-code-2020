filename = 'input.txt'

total = 0

with open(filename) as file:

    group_answer_lst = file.read().split('\n\n')

    for group_answer in group_answer_lst:
        answer = group_answer.replace('\n', '')
        answer_set = set(answer)
        total += len(answer_set)

print(total)
