# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился
# на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций.
# И далее в конце опять вывести на экран как таблицу.

from random import randint

n, m = int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))
my_random = [[randint(0, 100) for j in range(m)] for i in range(n)]
for line in my_random:
    print(line)
from random import shuffle

array = []
for i in my_random:
    for i2 in i:
        array.append(i2)
array2 = random.shuffle(array)
# for j in range(0, len(array), n):
#     number = array2[j: n + j]
#     if len(number) < n:
#         number = number + [None for m in range(n - len(number))]
#     print(list(number))
for line in my_random:
    print(array)