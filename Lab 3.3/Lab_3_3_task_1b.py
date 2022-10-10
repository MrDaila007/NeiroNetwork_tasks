print("b) Чтение из текстового файла:")
students = open('group_6a.txt')
i = 1
for line in students:
    print(str(i) + '. ' + line.strip())
    i += 1
students.close()
