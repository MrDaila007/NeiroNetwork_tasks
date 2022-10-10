a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(0, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))

# 2 1 3 4 5 6 6 6