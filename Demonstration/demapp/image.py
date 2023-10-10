from PIL import Image
import pandas as pd
import numpy as np
import os
import os.path

SIZEIMG = (224, 224)

train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")


def get_img_dataset(dataset: pd.DataFrame = train_dataset) -> np.ndarray:
    image_df: pd.DataFrame = dataset[' pixels'].copy()
    for i in range(len(image_df)):
        image_df[i] = np.fromstring(image_df[i], dtype=np.uint8, sep=' ')
        image_df[i] = np.reshape(image_df[i], (48, 48))
    return np.stack(image_df.to_numpy())


images_arr = get_img_dataset(train_dataset)


def resize_img(img_arr: np.ndarray) -> np.ndarray:
    resized_images: np.ndarray = np.empty((img_arr.shape[0], *SIZEIMG))
    for i in range(img_arr.shape[0]):
        image = Image.fromarray(img_arr[i], mode='L')
        resized_images[i] = np.asarray(image.resize(SIZEIMG))
    return resized_images
