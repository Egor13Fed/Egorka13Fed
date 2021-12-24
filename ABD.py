import math


def module(a):
    if a < 0:
        a = a * (-1)
    return a

print('Hello')
x = float(input('Введите x= '))
sin1 = math.sin(x)
sinus = sin1 / x
error = 0.001
print('Значение  левой части: ', sinus)
n = 0
a = 1
s = a
while True:

        k = ((-1) * (x ** 2)) / (4 * (n ** 2) + 10 * n + 6)
        a *= k
        s += a
        if abs(a) <= 0.0001:
            break

print('Значение правой части уравнения: ', s)
