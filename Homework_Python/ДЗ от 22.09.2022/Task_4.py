# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода
# три строки: первое число, второе число и операцию, после чего применяет операцию
# к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

try:
    x = float(input("Enter the first number: "))
    # d = round(3.14, 1)
    y = float(input("Enter the second number: "))
    z = input("Enter the operation sign: ")
    if y != 0:
        if z == '+':
            print(f'{round(x + y, 2)}')
        elif z == '-':
            print(f'{round(x - y, 2)}')
        elif z == '/':
            print(f'{round(x / y, 2)}')
        elif z == '*':
            print(f'{round(x * y, 2)}')
        elif z == 'mod':
            print(f'{round(x % y, 2)}')
        elif z == 'div':
            print(f'{x // y}')
        elif z == 'pow':
            print(f'{round(x ** y, 2)}')
        else:
            print("Enter the operation sign and don't show off")

    else:
        print("Division by 0!")

except:
    print("Enter an integer")