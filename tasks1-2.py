from pprint import pprint


def func_read_file():
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            numb_of_ingredients = int(file.readline())
            dish = []
            for _ in range(numb_of_ingredients):
                food, quantity, measure = file.readline().strip().split(' | ')
                dish.append({
                    'ingredient_name': food,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name] = dish
        return cook_book


result = func_read_file()
pprint(result, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}

    for dish in dishes:
        if dish not in result:
            print('Нет такого блюда')
            continue

        for ingredient in result[dish]:
            ingredients_list[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],
                'quantity': person_count * int(ingredient['quantity'])
            }
    pprint(ingredients_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
