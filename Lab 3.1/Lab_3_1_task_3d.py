import re
from collections import defaultdict
from collections import Counter

print("d) ")
words = []
for _ in range(int(input())):
    words.extend(input().split())
#
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке
#
alphabet = {
    {'A', 'a'},
    {'B', 'b'},
    {'C', 'c'},
    {'D', 'd'},
    {'E', 'e'},
    {'F', 'f'},
    {'G', 'g'},
    {'H', 'h'},
    {'I', 'i'},
    {'J', 'j'},
    {'K', 'k'},
    {'L', 'l'},
    {'M', 'm'},
    {'N', 'n'},
    {'O', 'o'},
    {'P', 'p'},
    {'Q', 'q'},
    {'R', 'r'},
    {'S', 's'},
    {'T', 't'},
    {'U', 'u'},
    {'V', 'v'},
    {'W', 'w'},
    {'X', 'x'},
    {'Y', 'y'},
    {'Z', 'z'},
}