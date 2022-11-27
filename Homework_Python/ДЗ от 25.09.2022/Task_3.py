# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
# выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

import random
first_list = []
for num in range(10):
    first_list.append(random.randrange(0, 100))
print(f'The first list: ', list(first_list))
print()


second_list = first_list[:]
list_length = len(second_list)
for i in range(list_length):
    random_index = random.randint(0, list_length - 1)
    temp = second_list[i]
    second_list[i] = second_list[random_index]
    second_list[random_index] = temp
print(f'The second list: ', second_list)
print()

result = [num for num in first_list if num in second_list]
print(f'Sorting and checking for matches: ', sorted(result))
print()