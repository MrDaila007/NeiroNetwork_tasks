import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# Устанавливаем seed для повторяемости результатов
numpy.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Преобразование размерности изображений
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
# Нормализация данных
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# Создаем последовательную модель
model = Sequential()

# Добавляем уровни сети
model.add(Dense(800, input_dim=784, activation="relu", kernel_initializer="normal"))
model.add(Dense(651, activation="relu", kernel_initializer="normal"))
model.add(Dense(500, activation="relu", kernel_initializer="normal"))
model.add(Dense(10, activation="softmax", kernel_initializer="normal"))

# Компилируем модель
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

# Обучаем сеть
model.fit(X_train, Y_train, batch_size=50, epochs=50, validation_split=0.2, verbose=2)

# Оцениваем качество обучения сети на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))

# Генерируем описание модели в формате json
model_json = model.to_json()
# Записываем модель в файл
json_file = open("mnist_model.json", "w")
json_file.write(model_json)
json_file.close()

model.save_weights("mnist_model.h5")

print ("Сохранили Model")


import numpy as np
from PIL import Image
#    Загружаем картинку из файла и преобразуем ее в массив Numpy.
im = Image.open('7py.png')
im_grey = im.convert('L')
im_array = np.array(im_grey)
im_array=np.reshape(im_array, (1, 784)).astype('float32')
#    Особенность набора данных MNIST заключается в том, что в нем для представления черного цвета используется код 255, а для белого - 0. Поэтому перед распознаванием изображения необходимо провести его инверсию:
# Инвертируем изображение
x = 255 - im_array
# Нормализуем изображение
x /= 255
#    Теперь изображение готово к распознаванию. Если наша обученная сеть содержится в переменной model, то для распознавания можно использовать следующий код:

# Нейронная сеть предсказывает класс изображения
prediction = model.predict(x)
print(prediction)
# Преобразуем ответ из категориального представления в метку класса
prediction = numpy.argmax(prediction, axis=1)
# Печатаем результат
print("Результат распознавания:")
print(prediction)