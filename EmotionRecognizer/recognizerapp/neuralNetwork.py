from numpy.typing import NDArray
import numpy as np
from tensorflow import keras
from keras.optimizers import Adam
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from image import read_images_from_dir


def make_image_array(images: list, emotions: list, directory: str):
    for emotion, img in read_images_from_dir(directory):
        emotions.append(emotion)
        images.append(img)
    images: NDArray = np.array(images)
    emotions: NDArray = keras.utils.to_categorical(emotions, 7)
    return images, emotions


img_train, emotions_train_categorical = make_image_array([], [], 'data/train/')
img_train = np.expand_dims(img_train, axis=3)
print(img_train.shape)
# img_test, emotions_test_categorical = make_image_array([], [], 'data/test/')
# print(img_test.shape)
print('data parsed correctly')

model = keras.Sequential([
    Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=(224, 224, 1)),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(128, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(256, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Flatten(),
    Dense(256, activation='relu'),
    Dense(256, activation='relu'),
    Dense(7, activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

his = model.fit(img_train, emotions_train_categorical, batch_size=19, epochs=10, validation_split=0.2)
model.save('model')
