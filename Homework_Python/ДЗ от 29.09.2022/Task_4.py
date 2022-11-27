# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Enter a number: '))
result = []
while number > 0:
    result.append(number % 2)
    number //= 2
result.reverse()
for i in result:
    print(i, end="")