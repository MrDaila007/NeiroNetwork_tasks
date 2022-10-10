
print("\nd) Чтение из текстового файла:")
students = open('students1cd.txt')
for line in students:
    print('{} {:.1}'.format(*line.strip().split()))
students.close()
