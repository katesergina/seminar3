# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def calc_diff_min_max_fraction(lst):
    min = None
    max = None

    for item in lst:
        fraction = item % 1
        if fraction == 0:
            continue
        
        if min is None or fraction < min:
            min = fraction
        if max is None or fraction > max:
            max = fraction
    
    return round(max - min, 2)

lst = [round(random.uniform(1.0, 10.0), 2) for _ in range(random.randint(1, 10))]
print(lst)
print(calc_diff_min_max_fraction(lst))

