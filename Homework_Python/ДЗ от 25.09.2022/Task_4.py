# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N и координаты двух точек и находит
# расстояние между ними в N-мерном пространстве.

from math import sqrt


class Point:
    def __init__(self, x, y, z):
        self.x1 = x
        self.y1 = y
        self.z1 = z

    def method(self, other):
        return sqrt((other.x1 - self.x1) ** 2 + (other.y1 - self.y1) ** 2 + (other.z1 - self.z1) ** 2)


p1 = [1, 2, 3]
p2 = [3, 2, 1]
point1 = Point(*p1)
point2 = Point(*p2)
print(point1.method(point2))