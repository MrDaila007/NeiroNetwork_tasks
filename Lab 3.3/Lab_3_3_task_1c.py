
print("\nc) Добавить к каждой фамилии имя:")
students = open('students1cd.txt', 'w')
title = 'Елисеев Данила\nКалинин Валентин\nКарпенко Ксения\n' \
        'Кондибор Никита\nКоновалов Андрей\nКохнюк Анастасия\n' \
        'Перепеча Данила\nПоличенков Максим\nПупко Ксения\n' \
        'Самостроенко Татьяна\nСергиенко Владислав\nХодос Юлия\n'
students.write(title)
students.close()

students = open('students1cd.txt')
for line in students:
    print(line.strip())
students.close()
