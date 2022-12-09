import numpy
import json
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# Устанавливаем seed для повторяемости результатов
numpy.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Преобразование размерности изображений
X_train = X_train.reshape(60000, 28,28,1)
X_test = X_test.reshape(10000, 28,28,1)
# Нормализация данных
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# Загружаем Model
from keras.models import model_from_json
# Загружаем данные об архитектуре сети из файла json
json_file = open("mnist_model_A.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель на основе загруженных данных
loaded_model = model_from_json(loaded_model_json)
# Загружаем веса в модель
loaded_model.load_weights("mnist_model_A.h5")

# Компилируем модель
loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

# Проверяем модель на тестовых данных
scores = loaded_model.evaluate(X_test, Y_test, verbose=0)
print("Точность модели на тестовых данных: %.2f%%" % (scores[1]*100))


import numpy as np
from PIL import Image
#    Загружаем картинку из файла и преобразуем ее в массив Numpy.
im = Image.open('8py.png')
im_grey = im.convert('L')
im_array = np.array(im_grey)
im_array=np.reshape(im_array, (1, 28,28)).astype('float32')
#    Особенность набора данных MNIST заключается в том, что в нем для представления черного цвета используется код 255, а для белого - 0. Поэтому перед распознаванием изображения необходимо провести его инверсию:
# Инвертируем изображение
x = 255 - im_array
# Нормализуем изображение
x /= 255
#    Теперь изображение готово к распознаванию. Если наша обученная сеть содержится в переменной model, то для распознавания можно использовать следующий код:

# Нейронная сеть предсказывает класс изображения
prediction = loaded_model.predict(x)
print(prediction)
# Преобразуем ответ из категориального представления в метку класса
prediction = numpy.argmax(prediction, axis=1)
# Печатаем результат
print("Результат распознавания:")
print(prediction)