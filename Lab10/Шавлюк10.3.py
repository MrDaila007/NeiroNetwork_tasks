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

json_file = open("10.2.json", "r")

loaded_model_json = json_file.read()

json_file.close()

loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("10.2.h5") 

loaded_model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy']) 

word_index = imdb.get_word_index()
words = text.text_to_word_sequence("bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful bad terrible awful")
x = np.array([word_index[word] if word in word_index else 0 for word in words])
print(x)
prediction = loaded_model.predict(np.array([x]))

print(prediction)

print(classes[np.argmax(prediction)]) 
