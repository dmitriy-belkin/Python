# задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def boolean_algebra(x, y, z):
    print(f'¬({x} V {y} V {z}) = \
¬{x} ⋀ ¬{y} ⋀ ¬{z} is \
{(not (x or y or z)) == (not x and not y and not z)}')
    return (not (x or y or z)) == (not x and not y and not z)


if (boolean_algebra(0, 0, 0)
    and boolean_algebra(0, 0, 1)
    and boolean_algebra(0, 1, 1)
    and boolean_algebra(1, 1, 1)
    and boolean_algebra(1, 0, 0)
    and boolean_algebra(1, 1, 0)
    and boolean_algebra(0, 1, 0)
    and boolean_algebra(1, 0, 1)):
    print("True")
else:
    print("False")