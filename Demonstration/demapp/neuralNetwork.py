from typing import Any
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from image import get_img_dir_generator


def make_image_array(images: list, emotions: list, directory: str):
    for emotion, img in get_img_dir_generator(directory):
        emotions.append(emotion)
        images.append(img)
    images: Any = np.array(images)
    emotions: Any = keras.utils.to_categorical(emotions, 7)
    return images, emotions


img_train, emotions_train_categorical = make_image_array([], [], 'data/train/')
print(img_train.shape)
img_test, emotions_test_categorical = make_image_array([], [], 'data/test/')
print(img_test.shape)

model = keras.Sequential([
    Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=(224, 224, 3)),
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(128, (3, 3), padding='same', activation='relu'),
    Conv2D(128, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(256, (3, 3), padding='same', activation='relu'),
    Conv2D(256, (3, 3), padding='same', activation='relu'),
    Conv2D(256, (3, 3), padding='same', activation='relu'),
    Conv2D(256, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    Conv2D(512, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Flatten(),
    Dense(4069, activation='relu'),
    Dense(4069, activation='relu'),
    Dense(7, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

his = model.fit(img_train, emotions_train_categorical, batch_size=19, epochs=3, validation_split=0.2)
model.save('model')
model_loaded = keras.models.load_model('model')
model.evaluate(img_test, emotions_test_categorical)
