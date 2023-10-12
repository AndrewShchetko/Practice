from typing import Iterator
from pathlib import Path
import pandas as pd
import numpy as np
import cv2

SIZEIMAGE: tuple[int, int] = (224, 224)
COUNTIMAGE: int = 28709
DIRECTORY: str = "data/train/"  # Image directory

train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")


def get_img_dataset(dataset: pd.DataFrame) -> np.ndarray:
    """
    Get image from string format
    """
    image_df: pd.DataFrame = dataset[' pixels'].copy()
    for i in range(len(image_df)):
        image_df[i] = np.fromstring(image_df[i], dtype=np.uint8, sep=' ')
        image_df[i] = np.reshape(image_df[i], (48, 48))
    return np.stack(image_df.to_numpy())


def resize_img_generator(img_arr: np.ndarray) -> Iterator[np.ndarray]:
    """
    Return generator with resized image
    """
    for i in range(img_arr.shape[0]):
        cv_image = cv2.cvtColor(img_arr[i], cv2.IMREAD_GRAYSCALE)
        resized_img = cv2.resize(cv_image, SIZEIMAGE)
        yield resized_img


def save_images(img_arr: np.ndarray, dataset: pd.DataFrame) -> None:
    """
    Save images png format in DIRECTORY
    File name: {index file in dataset}_{emotion}.png
    """
    filenames: list[str] = [DIRECTORY + str(i) + "_" + str(dataset.iloc[i, 0]) + ".png"
                            for i in range(dataset.shape[0])]
    for item, image in zip(range(COUNTIMAGE), resize_img_generator(img_arr)):
        cv2.imwrite(filenames[item], image)


save_images(get_img_dataset(train_dataset), train_dataset)


def get_img_dir_generator(directory: str) -> Iterator[tuple[int, pd.DataFrame]]:
    """
    Read images from directory and return emotion and image.
    """
    p = Path(directory)
    for file in p.iterdir():
        image = cv2.imread(str(file))
        emotion = int(file.name.split(".")[0].split("_")[1])
        yield emotion, np.asarray(image)
