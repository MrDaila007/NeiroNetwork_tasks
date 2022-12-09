import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.models import model_from_json

# Размер изображения
img_rows, img_cols = 28, 28

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Преобразование размерности изображений
X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
input_shape = (1, img_rows, img_cols)

# Нормализация данных
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# Загружаем данные об архитектуре сети из файла json
json_file = open("mnist_model_conv.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель на основе загруженных данных
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("mnist_model_conv.h5")

# Компилируем модель
loaded_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Проверяем модель на тестовых данных
scores = loaded_model.evaluate(X_test, Y_test, verbose=0)
print("Точность модели на тестовых данных: %.2f%%" % (scores[1]*100))

import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt

img_path = ('8py.png')
img = image.load_img(img_path, target_size=(28, 28), grayscale=True)
plt.imshow(img, cmap='gray')
plt.show()

# Преобразуем картинку в массив и нормализуем
x = image.img_to_array(img)
x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)

prediction = loaded_model.predict(x)
print(prediction)
prediction = numpy.argmax(prediction, axis=1)
print(prediction)
