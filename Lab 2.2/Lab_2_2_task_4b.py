print("Swap two words")
# one two
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
theard_word = second_word + ' ' + first_word
print(theard_word)