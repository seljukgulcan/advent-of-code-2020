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

allergic_ing_set = set()

allergy2ing_set = dict()
allergy2ing = dict()

for allergy in all_allergy_set:

    allergic_food_lst = allergy2food[allergy]
    common_ing_set = allergic_food_lst[0].ingredient_set

    for food in allergic_food_lst:
        common_ing_set = common_ing_set & food.ingredient_set

    allergy2ing_set[allergy] = common_ing_set

for _ in range(len(all_allergy_set)):

    for allergy, ing_set in allergy2ing_set.items():
        if len(allergy2ing_set[allergy]) == 1:
            ingredient = list(ing_set)[0]
            allergy2ing[allergy] = ingredient
            break
    else:
        raise ValueError('Couldnt find single ingredient for the allergy {}'.format(allergy))

    for allergy, ing_set in allergy2ing_set.items():
        ing_set.discard(ingredient)

matching_lst = list(allergy2ing.items())
matching_lst.sort()

for allergy, ingredient in matching_lst:
    print(ingredient, end=',')
print()
