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


def get_img_dataset(dataset: pd.DataFrame = train_dataset) -> np.ndarray:
    """
    Get image from string format.
    Another shit function.
    """
    image_df: pd.DataFrame = dataset[' pixels'].copy()
    for i in range(len(image_df)):
        image_df[i] = np.fromstring(image_df[i], dtype=np.uint8, sep=' ')
        image_df[i] = np.reshape(image_df[i], (48, 48))
    return np.stack(image_df.to_numpy())


images_arr = get_img_dataset(train_dataset)


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


save_images(resized_images, train_dataset)


def get_img_dir() -> pd.DataFrame:  # MY COMPUTER FREEZES CAUSE OF THIS PIECE OF SHIT
    """
    This is shit function for fucking dataset of fucking coursework.
    Read images from DIRECTORY and return dataframe.
    """
    images_arr: np.ndarray = np.empty((COUNTIMAGE, *SIZEIMAGE))
    emotion: np.ndarray = np.empty(COUNTIMAGE)
    count_image = 0
    for filename in os.listdir(DIRECTORY):
        f = os.path.join(DIRECTORY, filename)
        image = Image.open(f)
        images_arr[count_image] = np.asarray(image)
        emotion[count_image] = int(filename.split(".")[0].split("_")[1])
        # split string like [0_0 , .png] then [0,0]
        count_image += 1

    return pd.DataFrame(data=[emotion.T, pd.DataFrame(images_arr)])

# data = get_img_dir()
# print(data)
