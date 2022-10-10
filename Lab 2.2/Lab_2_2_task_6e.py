index_of_max = 0
a = [int(i) for i in input().split()]
b = []
c = []
count1 = 0
count2 = 0
count_of_max = 0

for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    elif a[i] == a[index_of_max]:
        b[count1] = a[index_of_max]
        c[count1] = a[i]
        count1 += 1
        c[count2] = i
        b[count1] = a[i]
        count2 += 1
        b[count1] = a[i]
        count_of_max += 1


print(a[index_of_max], index_of_max)