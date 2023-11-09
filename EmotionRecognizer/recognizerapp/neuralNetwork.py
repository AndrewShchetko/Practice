from numpy.typing import NDArray
import numpy as np
from tensorflow import keras
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras import layers, models
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
# img_test, emotions_test_categorical = make_image_array([], [], 'data/test/')
# print(img_test.shape)
print('data parsed correctly')
img_train = custom_preprocess_input(img_train)
# img_test = custom_preprocess_input(img_test)
print('end of preprocess input')

# base_model = VGG19(weights='imagenet', include_top=False)
#
# out = base_model.output
# out = GlobalAveragePooling2D()(out)
# out = Dense(1024, activation='relu')(out)
# out = Dense(512, activation='relu')(out)
# predictions = Dense(7, activation='softmax')(out)
#
# model = Model(inputs=base_model.input, outputs=predictions)
# for layer in base_model.layers:
#     layer.trainable = False
#
# model.compile(
#     optimizer=Adam(learning_rate=0.001),
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

for layer in base_model.layers:
    layer.trainable = False

model = models.Sequential()
model.add(base_model)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(7, activation='softmax'))

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

his = model.fit(img_train, emotions_train_categorical, batch_size=19, epochs=10, validation_split=0.2)
model.save('model')
