import math


def hello():
    print('Hello, world!')


def fibon(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    print(b)


def discr(a, b, c):
    D = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + D) / 2 * a
    x2 = (-b - D) / 2 * a
    print(f'x1 = {x1}', f'x2 = {x2}', sep='\n')
