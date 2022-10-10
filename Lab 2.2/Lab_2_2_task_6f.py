def move_zeros(a):
    j = 0
    for v in a:
        if v != '0':
            a[j] = v
            j += 1
    for k in range(j, len(a)):
        a[k] = '0'

s = input().split()
move_zeros(s)
print(s)