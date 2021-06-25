from pprint import pprint
with open("recipes.txt", encoding="UTF-8") as file:
  cook_book = {}
  for line in file:
    dish = file.readline().strip()
    # print(dish)
    ingredients = []
    number_of_ing = int(file.readline().strip())
    # print(number_of_ing)
    number = 0
    while number < number_of_ing:
      line = file.readline().strip()
      value_list = line.split(' | ')
      value_list[1] = int(value_list[1])
      # print(value_list)
      key_list = ['ingredient_name', 'quantity', 'measure']
      my_dict = dict(zip(key_list, value_list))
      # print(my_dict)
      ingredients.append(my_dict)
      # print(ingredients)
      number += 1
      cook_book[dish] = ingredients
  pprint(cook_book)