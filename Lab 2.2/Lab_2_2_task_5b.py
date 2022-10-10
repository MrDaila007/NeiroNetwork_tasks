print("Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.")
# 2 1 4 2 4 6 1 10
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])