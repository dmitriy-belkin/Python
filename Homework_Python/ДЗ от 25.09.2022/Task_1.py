# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

'''
Solution No. 1
'''
try:
    number = float(input('Enter a number: '))
    summ = 0
    for i in list(str(number)):
        if i != '.':
            summ += float(i)
    print(summ)
except:
    print('Attention, enter a number')

'''
Solution No. 2
'''
try:
    number = input('Enter a number: ')
    summ = 0
    for i in number:
        if i != '.':
            summ += float(i)
    print(summ)
except:
    print('Attention, enter a number')