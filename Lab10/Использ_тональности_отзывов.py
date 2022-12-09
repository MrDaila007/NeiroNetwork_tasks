import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM, SpatialDropout1D
from keras.datasets import imdb
from keras.models import model_from_json
from keras.preprocessing import text

# Устанавливаем seed для повторяемости результатов
np.random.seed(42)
# Максимальное количество слов (по частоте использования)
max_features = 5000
# Максимальная длина рецензии в словах
maxlen = 80

json_file = open("cc_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("cc_model.h5")
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print ("Загрузили Model")

# ***** Загружаем изображение в Keras:
x = text.one_hot('C:/Users/Danila/PycharmProjects/NeiroNetworks_CONDA/Lab10/999.txt',
                                 5000,
                                 filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
                                 lower=True,
                                 split=" ")


# Запускаем распознавание объекта:
# prediction = loaded_model.predict(np.array[x])
# print(prediction)
print(x)

