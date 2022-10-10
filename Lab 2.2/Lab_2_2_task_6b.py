def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

# замена первых букв на заглавные
# test task
source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))