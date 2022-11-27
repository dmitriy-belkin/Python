# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools as it
import time
start = time.time()

def ratios_list(k):
    indicator = [randint(0, 10) for i in range(k + 1)]
    if indicator[0] == 0:
        indicator[0] = randint(1, 10)
    return indicator


def list_of_sums_of_monomials(meaning, indicator):
    operation = ['*x^']*(meaning-1) + ['*x']
    sum_of_monomials = [[a, b, c] for a, b, c in it.zip_longest(
        indicator, operation, range(meaning, 1, -1), fillvalue='') if a != 0]
    for x in sum_of_monomials:
        x.append(' + ')
    sum_of_monomials = list(it.chain(*sum_of_monomials))
    sum_of_monomials[-1] = ' = 0'
    return "".join(map(str, sum_of_monomials)).replace(' 1*x', ' x')


meaning = randint(2, 5)
indicator = ratios_list(meaning)
sum_of_monomials = list_of_sums_of_monomials(meaning, indicator)
print(sum_of_monomials)

with open('Volgograd.txt', 'w') as data:
    data.write(sum_of_monomials)
fin = time.time()
print(fin - start)