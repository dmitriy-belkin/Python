# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint
num = [randint(0, 50) for i in range(20)]


def get_unique_numbers(num):
    empty_list = []
    non_repeating_numbers = set(num)

    for i in non_repeating_numbers:
        empty_list.append(i)

    return empty_list


print(get_unique_numbers(num))