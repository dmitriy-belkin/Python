# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint
n, m = int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))
my_random = [[randint(0, 100) for j in range(m)] for i in range(n)]
print(my_random)

array = []
for i in my_random:
    for i2 in i:
        array.append(i2)
array2 = sorted(array)
for j in range(0, len(array), n):
    number = array2[j: n + j]
    if len(number) < n:
        number = number + [None for m in range(n - len(number))]
    print(list(number))