# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

try:
    i = 1
    ls = []
    while i < 3:
        ls.append(int(input(f'Enter {i} number: ')))
        i += 1

    if ls[0] > ls[1]:
        larger_number = ls[0]
    else:
        larger_number = ls[1]

    while (True):
        if (larger_number % ls[0] == 0) and (larger_number % ls[1] == 0):
            result = larger_number
            break
        larger_number += 1

    print(f'The smallest common multiple: {result}')

except:
    print("Enter an integer")