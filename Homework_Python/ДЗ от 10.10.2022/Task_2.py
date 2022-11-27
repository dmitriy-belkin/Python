# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

import re

input_str = input()

initial_operations = r"\((.+?)\)"
secondary_operations = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

operations = {
    "*": lambda a, b: str(float(a) * float(b)),
    "/": lambda a, b: str(float(a) / float(b)),
    "+": lambda a, b: str(float(a) + float(b)),
    "-": lambda a, b: str(float(a) - float(b)),
    "^": lambda a, b: str(float(a)**float(b))
}


def actions_with_operations(formulation: str) -> str:

    while (sameness := re.search(initial_operations, formulation)):
        formulation: str = formulation.replace(
            sameness.group(0), actions_with_operations(sameness.group(1)))

    for symbol, action in operations.items():
        while (sameness := re.search(secondary_operations.format(symbol), formulation)):
            formulation: str = formulation.replace(sameness.group(0), action(*sameness.groups()))

    return formulation


print(actions_with_operations(input_str))