from keras.layers import GlobalAveragePooling2D
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import  Dense
from keras.models import Model
from keras import initializers
# Размер изображений
img_width, img_height = 150, 150
# Путь к каталогу с изображениями для обучения
train_data_dir = 'C:/Users/Yaroslav/Desktop/train'
# Путь к каталогу с изображениями для валидации
validation_data_dir = 'C:/Users/Yaroslav/Desktop/train'
# Количество изображений для обучения
nb_train_samples = 20
# Количество изображений для валидации
nb_validation_samples = 800
# Количество эпох
epochs = 1
# Размер выборки
batch_size = 16


# Загружаем сеть VGG16 без части, которая отвечает за классификацию
base_model = applications.VGG16(weights='imagenet', include_top=False)

# Добавляем слои классификации
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu',
          kernel_initializer=initializers.RandomUniform(minval=-0.0019, maxval=0.0019, seed=None))(x)
# 1024 - число нейронов на этом слое
# Выходной слой с двумя нейронами для классов "кот" и "собака"
predictions = Dense(2, activation='softmax')(x)

# Составляем сеть из двух частей
model = Model(inputs=base_model.input, outputs=predictions)

# "Замораживаем" сверточные уровни сети VGG16
# Обучаем только вновь добавленные слои
for layer in base_model.layers:
    layer.trainable = False

# Компилируем модель
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Создаем генератор данных для обучения
datagen = ImageDataGenerator(rescale=1. / 255)
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')


# Создаем генератор данных для валидации
validation_generator = datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')


# Обучаем модель с помощью генератора
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples)

model_json = model.to_json()

# Записываем модель в файл
json_file = open("vgg16_cat_dogstest.json", "w")
json_file.write(model_json)
json_file.close()

# Сохраняем веса модели
model.save_weights("vgg16_cat_dogstest.h5")