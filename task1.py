# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

def sum_odd_position(lst):
    sum = 0
    for i in range(0, len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    return sum

lst = [random.randint(0,10) for i in range(random.randint(1, 5))]
print(lst)
print(sum_odd_position(lst))

