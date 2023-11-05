from numpy.typing import NDArray
import numpy as np
from tensorflow import keras
from keras.applications.vgg19 import VGG19, preprocess_input
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.optimizers import Adam
from image import read_images_from_dir


def make_image_array(images: list, emotions: list, directory: str):
    for emotion, img in read_images_from_dir(directory):
        emotions.append(emotion)
        images.append(img)
    images: NDArray = np.array(images)
    emotions: NDArray = keras.utils.to_categorical(emotions, 7)
    return images, emotions


def custom_preprocess_input(images: NDArray):
    for i in range(len(images)):
        images[i] = preprocess_input(images[i])
    return images


img_train, emotions_train_categorical = make_image_array([], [], 'data/train/')
print(img_train.shape)
img_test, emotions_test_categorical = make_image_array([], [], 'data/test/')
print(img_test.shape)
print('data parsed correctly')
img_train = custom_preprocess_input(img_train)
img_test = custom_preprocess_input(img_test)
print('end of preprocess input')

base_model = VGG19(weights='imagenet', include_top=False)

out = base_model.output
out = GlobalAveragePooling2D()(out)
out = Dense(1024, activation='relu')(out)
out = Dense(512, activation='relu')(out)
predictions = Dense(7, activation='softmax')(out)

model = Model(inputs=base_model.input, outputs=predictions)
for layer in base_model.layers:
    layer.trainable = False

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

his = model.fit(img_train, emotions_train_categorical, batch_size=32, epochs=10, validation_split=0.2)
model.save('model')
