from typing import Iterator
from pathlib import Path
import pandas as pd
import numpy as np
import cv2

SIZEIMAGE: tuple[int, int] = (224, 224)

train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")


<<<<<<< HEAD
def get_img_dataset(dataset: pd.DataFrame) -> np.ndarray:
    """
    Get image from string format
=======
def get_pixel_array(dataset: pd.DataFrame) -> np.ndarray:
    """
    Get image from string format in dataset.
    Another shit function.
>>>>>>> 7300f32 (fix(image)!: rename get_img_dataset to get_pixel_array)
    """
    image_df: pd.DataFrame = dataset[' pixels'].copy()
    for i in range(len(image_df)):
        image_df[i] = np.fromstring(image_df[i], dtype=np.uint8, sep=' ')
        image_df[i] = np.reshape(image_df[i], (48, 48))
    return np.stack(image_df.to_numpy())


def resize_images(img_arr: np.ndarray) -> Iterator[np.ndarray]:
    """
    Return generator with resized image
    """
    for i in range(img_arr.shape[0]):
        cv_image = cv2.cvtColor(img_arr[i], cv2.IMREAD_GRAYSCALE)
        resized_img = cv2.resize(cv_image, SIZEIMAGE)
        yield resized_img


def save_images(dataset: pd.DataFrame, directory: str) -> None:
    """
    Save images png format in directory
    Path and file name: {directory}/{dataset[" Usage"].lower()}/{index file in dataset}_{emotion}.png
    """
    if "/" not in directory:
        directory += "/"
    img_arr = get_pixel_array(dataset)
    Path(directory + dataset[" Usage"][0].lower() + "/").mkdir(parents=True, exist_ok=True)

    filenames: list[str] = [directory + dataset[" Usage"][0].lower() + "/"
                            + str(i) + "_" + str(dataset.iloc[i, 0]) + ".png"
                            for i in range(dataset.shape[0])]
    for item, image in zip(range(dataset.shape[0]), resize_images(img_arr)):
        cv2.imwrite(filenames[item], image)


<<<<<<< HEAD
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
=======
def read_images_from_dir(directory: str) -> Iterator[tuple[str,int, pd.DataFrame]]:
    """
    Read images from directory and return type of dataset, emotion and image.
    """
    p = Path(directory)
    for path in p.glob("*/*.png"):
        image = cv2.imread(str(path))
        emotion = int(path.name.split(".")[0].split("_")[1])
        yield str(path.parent).lstrip(directory + "/"), emotion, np.asarray(image)


save_images(pd.concat([train_dataset, test_dataset], ignore_index=True), "data")
>>>>>>> b5c0546 (fix(image)!: rewrite function get_img_dir_generator)
