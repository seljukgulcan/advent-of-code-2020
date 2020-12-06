filename = 'input.txt'

total = 0

with open(filename) as file:

    group_answer_lst = file.read().split('\n\n')

    for group_answer in group_answer_lst:
        person_answer_lst = group_answer.split('\n')

        answer_intersection = set(person_answer_lst[0])

        for person_answer in person_answer_lst[1:]:
            answer_intersection = answer_intersection.intersection(set(person_answer))

        total += len(answer_intersection)

print(total)
