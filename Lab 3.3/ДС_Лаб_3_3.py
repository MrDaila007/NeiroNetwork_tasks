import math
import random
import mymodule

print("Задание 1)")

print("\na) Запись в текстовый файл:")
students = open('resources/students1ab.txt', 'w')
title = 'Елисеев\nКалинин\nКарпенко\n' \
        'Кондибор\nКоновалов\nКохнюк\n' \
        'Перепеча\nПоличенков\nПупко\n' \
        'Самостроенко\nСергиенко\nХодос\n'
students.write(title)
students.close()

students = open('resources/students1ab.txt')
print(students.read())
students.close()

print("b) Чтение из текстового файла:")
students = open('resources/students1ab.txt')
i = 1
for line in students:
    print(str(i) + ') ' + line.strip())
    i += 1
students.close()

print("\nc) Добавить к каждой фамилии имя:")
students = open('resources/students1cd.txt', 'w')
title = 'Елисеев Данила\nКалинин Валентин\nКарпенко Ксения\n' \
        'Кондибор Никита\nКоновалов Андрей\nКохнюк Анастасия\n' \
        'Перепеча Данила\nПоличенков Максим\nПупко Ксения\n' \
        'Самостроенко Татьяна\nСергиенко Владислав\nХодос Юлия\n'
students.write(title)
students.close()

students = open('resources/students1cd.txt')
for line in students:
    print(line.strip())
students.close()

print("\nd) Чтение из текстового файла:")
students = open('resources/students1cd.txt')
for line in students:
    print('{} {:.1}'.format(*line.strip().split()))
students.close()

print("\nЗадание 2)")

print("\na) Логарифм:")
print(math.log2(15), 'and', math.log(15, 2))

print("\nb) Четыре раза одно и то же число на (0; 1):")
for i in range(0, 4):
    random.seed(10)
    print(random.random())

print("\nc) Cписок имен")
print(*dir(), sep='\n')

print("\nd) Свой модуль:")
mymodule.hello()
mymodule.fibon(10)
mymodule.discr(1, 10, -39)
