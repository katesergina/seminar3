# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import random

def calc_pairs_prod(lst):
    result = []
    for i in range(0, len(lst)):
        pair_index = len(lst) - 1 - i
        if pair_index < i:
            return result
        prod = lst[i] * lst[pair_index]
        result.append(prod)
    return result

lst = [random.randint(0,10) for i in range(random.randint(1, 10))]
print(lst)
print(calc_pairs_prod(lst))

