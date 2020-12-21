from collections import defaultdict

filename = 'input.txt'

class Food:

    def __init__(self, ingredient_set, allergy_set):
        self.ingredient_set = ingredient_set
        self.allergy_set = allergy_set


allergy2food = defaultdict(list)
food_lst = []
all_ingredient_set = set()
all_allergy_set = set()

with open(filename) as file:
    for line in file:
        ingredient_str, allergy_str = line.split(' (contains ')
        ingredient_set = set(ingredient_str.split())
        allergy_set = set(allergy_str.strip()[:-1].split(', '))

        all_ingredient_set = all_ingredient_set | ingredient_set
        all_allergy_set = all_allergy_set | allergy_set

        food = Food(ingredient_set, allergy_set)
        food_lst.append(food)
        for allergy in allergy_set:
            allergy2food[allergy].append(food)

print('The number of foods: {}'.format(len(food_lst)))
print('The number of ingredients: {}'.format(len(all_ingredient_set)))
print('The number of allergies: {}'.format(len(all_allergy_set)))
print()

allergic_ing_set = set()

for allergy in all_allergy_set:

    # print(allergy)
    allergic_food_lst = allergy2food[allergy]
    common_ing_set = allergic_food_lst[0].ingredient_set

    for food in allergic_food_lst:
        common_ing_set = common_ing_set & food.ingredient_set

    # print(common_ing_set)
    allergic_ing_set = allergic_ing_set | common_ing_set

print(len(allergic_ing_set))

non_allergic_ing_set = all_ingredient_set - allergic_ing_set

print(len(non_allergic_ing_set))

answer = 0
for food in food_lst:
    answer += len(non_allergic_ing_set & food.ingredient_set)
print(answer)
