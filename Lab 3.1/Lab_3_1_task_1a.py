import re
from collections import defaultdict
from collections import Counter

print("Задание 1)")
print("a) ")
t = (1, [2, 3])
l = list(t)
l[1].append(4)
t = tuple(l)
print(t)