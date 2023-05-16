# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# import random

# def convert_to_binary(n):
#     b = ''
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
#     return b

# number = random.randint(1, 10)
# number = 2
# print(number)
# print(convert_to_binary(number))

n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)