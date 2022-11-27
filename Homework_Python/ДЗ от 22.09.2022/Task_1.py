# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def day_of_week(a):
    day = False
    if 1 < a < 6:
        day = True
        return day

try:
    number = int(input("Enter a number from 1 to 7: "))
    if number > 7 or number < 0:
        print("Enter a number according to the condition")
    else:
        if day_of_week(number):
            print("This day is a weekday")
        else:
            print("This day is a day off")
except:
    print("Enter an integer")