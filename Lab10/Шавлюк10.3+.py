import numpy as np 
from keras.preprocessing import image
from keras.models import Model
from keras.models import model_from_json 
from keras.layers import Dense, GlobalAveragePooling2D
from keras import applications
from keras.applications.vgg16 import preprocess_input 
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model
from keras.preprocessing import text
from keras.preprocessing import sequence
from keras.datasets import imdb

from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM, SpatialDropout1D

json_file = open("cc_model.json", "r")

loaded_model_json = json_file.read()

json_file.close()

loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("cc_model.h5")

loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

word_index = imdb.get_word_index()
words = text.text_to_word_sequence("If you like  ")

x = np.array([word_index[word] if word in word_index else 0 for word in words])
print(x)

prediction = loaded_model.predict(np.array([x]))

print(prediction)


