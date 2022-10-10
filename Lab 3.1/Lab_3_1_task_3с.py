import re
from collections import defaultdict
from collections import Counter

print("c) ")
def most_common(t):
   return sorted((x for x in Counter(t.split()).items()), key=lambda x: (-x[1], x[0]))[0][0]
text = ('Дан текст: в первой строке задано число строк, далее идут сами строки. '
        'Выведите слово, которое в этом тексте встречается чаще всего. '
        'Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.')
d = defaultdict(int)
text = input()
for word in re.sub(r'\W', ' ', text).split():
    d[word] += 1
res = min(d.items(), key=lambda x: (-x[1], x[0]))[0]
print(res)