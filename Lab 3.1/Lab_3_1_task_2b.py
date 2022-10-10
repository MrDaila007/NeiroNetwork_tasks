import re
from collections import defaultdict
from collections import Counter

print("b) ")
a = [1, 2, 3, 1, 2, 3, 3, 2, 1, 3, 2, 1]
l = list(a)  # (input().split())
newlist = set()
for i in l:
    # print(len(l))
    if (i%2) != 0:
        print('YES' if i in newlist else 'NO')
        newlist.add(i)
