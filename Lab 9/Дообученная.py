import numpy as np
import keras
from keras.models import model_from_json
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
#from scipy.misc import toimage

# Список классов
classes = ['кот', 'собака']
#C:\Users\Danila\PycharmProjects\NeiroNetworks_CONDA\vgg16_cat_dogs.json
json_file = open("C:/Users/Danila/PycharmProjects/NeiroNetworks_CONDA/vgg16_cat_dogs.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("C:/Users/Danila/PycharmProjects/NeiroNetworks_CONDA/vgg16_cat_dogs.h5")

loaded_model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

img = keras.utils.load_img('C:/Users/Danila/PycharmProjects/NeiroNetworks_CONDA/Lab 9/cat1.jpg', target_size=(224, 224))

x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

prediction = loaded_model.predict(x)

print(prediction)
print(classes[np.argmax(prediction)])