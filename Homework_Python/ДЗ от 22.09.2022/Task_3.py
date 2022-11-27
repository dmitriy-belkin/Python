# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = int(input("Enter the first coordinate: "))
    y = int(input("Enter the second coordinate: "))
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print("1st quarter")
        elif x > 0 and y < 0:
            print("2nd quarter")
        elif x < 0 and y < 0:
            print("3rd quarter")
        else:
            print("4th quarter")
    else:
        print("None of the coordinates should be equal to 0")
except:
    print("Enter an integer")