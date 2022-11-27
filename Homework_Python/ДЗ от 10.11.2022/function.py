# -*- coding: utf-8 -*-
import numpy as np
from numpy import sin, cos, sign, abs
import matplotlib.pyplot as plt

colors = {
    -1: 'blue',
    0: 'black',
    1: 'red'}

# поиск делением пополам


def get_bissect(f, a, b, err=1):
    m = (a + b) / 2
    if np.abs(f(m)) < err:
        return m, f(m)
    elif np.sign(f(a)) == np.sign(f(m)):
        return get_bissect(f, m, b, err)
    elif np.sign(f(b)) == np.sign(f(m)):
        return get_bissect(f, a, m, err)

# Определение функции


def func(arg):
    return 12 * arg ** 4 * sin(cos(arg)) - 18 * arg ** 3 + 5 * arg ** 2 + 10 * arg - 30

# Производная функции


def d_fun(arg):
    h = 1e-5
    return (func(arg + h) - func(arg - h)) / (2 * h)


plt.style.use('seaborn-v0_8')
fig = plt.figure(1)
plt.title("График функции, общий вид.")
x = np.arange(-50, 50, 0.1)
y = func(x)
plt.plot(x, y, 'g')


fig = plt.figure(2)
x = np.arange(-20, 20, 0.1)
y = func(x)
plt.xlim((-20, 20))
plt.ylim((-100, 100))
plt.title("График функции, знаки значений, корни.")

for i in range(x.size - 1):
    if sign(y[i]) == sign(y[i+1]):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], colors[sign(y[i])])
    else:
        x_r, y_r = get_bissect(func, x[i], x[i + 1])
        plt.plot([x[i], x_r], [y[i], y_r], colors[sign(y[i])])
        plt.plot([x[i+1], x_r], [y[i+1], y_r], colors[sign(y[i+1])])
        plt.plot(x_r, y_r, 'ko')


fig = plt.figure(3)
x = np.arange(-20, 20, 0.1)
y = func(x)
plt.xlim((-20, 20))
plt.ylim((-100, 100))
plt.title("График функции и интервалы монотонности.")

for i in range(x.size - 1):
    if sign(d_fun(x[i])) == sign(d_fun(x[i + 1])):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], colors[sign(d_fun(x[i]))])
    else:
        x_p, _ = get_bissect(d_fun, x[i], x[i + 1])
        plt.plot([x[i], x_p], [y[i], func(x_p)], colors[sign(y[i])])
        plt.plot([x[i + 1], x_p], [y[i + 1], func(x_p)],
                 colors[sign(y[i + 1])])
        plt.plot(x_p, func(x_p), 'ko')

plt.show()