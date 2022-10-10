print("Задание 1)")

print("\na) Запись в текстовый файл:")
students = open('group_6a.txt', 'w')
title = 'Елисеев\nКалинин\nКарпенко\n' \
        'Кондибор\nКоновалов\nКохнюк\n' \
        'Перепеча\nПоличенков\nПупко\n' \
        'Самостроенко\nСергиенко\nХодос\n'
students.write(title)
students.close()

students = open('group_6a.txt')
print(students.read())
students.close()
