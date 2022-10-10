my_file = open("group_6a.txt", "w")
print("Задние 1а")
my_file.write(" Елисеев Данила\n Калинин Валентин\n Карпенко Ксения\n"
              " Кондибор Никита\n Коновалов Андрей\n Кохнюк Анастасия\n Перепеча Данила\n"
              " Поличенков Максим\n Пупко Ксения\n Самостроенко Татьяна\n"
              " Сергиенко Владислав\n Ходос Юлия\n")
my_file.close()
my_file = open("group_6a.txt")
my_string = my_file.read()
print("Было прочитано:")
print(my_string)
my_file.close()
