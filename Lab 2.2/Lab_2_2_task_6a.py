s = input("Введите строку:")
vowels = 0
consonants = 0
for i in s:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print("Vowels %i\nConsonants %i" % (vowels, consonants))

############################################################
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
Consonants = len(s) - count
print("Количество гласных равно: ", count)
print("Количество согласных равно: ", Consonants)
