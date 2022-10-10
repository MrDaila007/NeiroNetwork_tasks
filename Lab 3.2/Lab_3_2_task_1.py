import math
import re


print("Задание 1)")


print("a) Введите координаты 2 точек")


def distance(x1, y1, x2, y2):
    dist = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return dist


try:
    x1, y1, x2, y2 = map(float, input().split())
    d = distance(x1, y1, x2, y2)
except TypeError as e:
    print('Type Error:', e)
except ZeroDivisionError:
    print('Division on zero!')
except ValueError as e:
    print('Value Error:', e)
else:
    print(d)


print("b) Введите число и степень")


def power(a, n):
    x = 1
    while n != 0:
        x *= a
        n -= 1
    return x


a, n = map(int, input().split())
print(power(a, n), 'and', pow(a, n))


print("c)")


def capitalize(w):
    w_new = chr(ord(w[0]) - 32) + w[1:]
    return w_new


w = input("Введите слово: ")
print(capitalize(w))

arr = "".join(re.findall(r'[ A-Za-z]', input("Введите предложение: "))).split()
arr_new = []
for i in arr:
    arr_new.append(capitalize(i))
print(*arr_new)


print("d) Введите что-нибудь")


def max2(args, key=lambda x: x):
    result = args[0]
    for item in args[1:]:
        if key(item) > key(result):
            result = item
    return result


a = input().split()
print('Maximum:', max2(a), 'and', max(a))
