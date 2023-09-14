import numpy as np
import pandas as pd
from tensorflow import keras
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

emotions_train = pd.read_csv('train.csv')
emotions_test = pd.read_csv('test.csv')

x_train, y_train = emotions_train.pop(' pixels'), emotions_train.pop('emotion')
x_test, y_test = emotions_test.pop(' pixels'), emotions_test.pop('emotion')

for i in range(len(x_train)):
    x_train[i] = np.fromstring(x_train[i], dtype=np.uint8, sep=' ')
    x_train[i] = np.reshape(x_train[i], (48, 48))
x_train = x_train / 255
x_train = x_train.values.tolist()
x_train = np.array(x_train)

for i in range(len(x_test)):
    x_test[i] = np.fromstring(x_test[i], dtype=np.uint8, sep=' ')
    x_test[i] = np.reshape(x_test[i], (48, 48))
x_test = x_test / 255
x_test = x_test.values.tolist()
x_test = np.array(x_test)

x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)
y_train_categorical = keras.utils.to_categorical(y_train, 7)
y_test_categorical = keras.utils.to_categorical(y_test, 7)

model = keras.Sequential([
    Conv2D(96, (3, 3), padding='same', activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(192, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Conv2D(384, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2), strides=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(7, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

his = model.fit(x_train, y_train_categorical, batch_size=19, epochs=3, validation_split=0.2)
model.save('model')
# model_loaded = keras.models.load_model('model')
# model.evaluate(x_test, y_test_categorical)

