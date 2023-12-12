from typing import Iterator
from pathlib import Path
import pandas as pd
import numpy as np
import cv2
from PIL import Image

# train_dataset = pd.read_csv("train.csv")
# test_dataset = pd.read_csv("test.csv")


def get_pixel_array(dataset: pd.DataFrame) -> np.ndarray:
    """
    Get image from string format in dataset.
    """
    image_df: pd.DataFrame = dataset[' pixels'].copy()
    for i in range(len(image_df)):
        image_df[i] = np.fromstring(image_df[i], dtype=np.uint8, sep=' ')
        image_df[i] = np.reshape(image_df[i], (48, 48))
    return np.stack(image_df.to_numpy())


def resize_images(images_array: np.ndarray, new_image_size: tuple = (224, 224), image_format: str = 'gray') \
        -> Iterator[np.ndarray]:
    """
    Return generator with resized image rgb format

    Parameters
    ------------------------
    images_array: np.ndarray
    new_image_size: tuple[int, int], default = (224, 224),
    image_format: {'gray', 'bgr', 'rgb'},  default ='gray'
    """
    image_formats = {'rgb': cv2.COLOR_GRAY2RGB, 'bgr': cv2.COLOR_GRAY2BGR, 'gray': cv2.IMREAD_GRAYSCALE}

    for i in range(images_array.shape[0]):
        cv_image = cv2.cvtColor(images_array[i], image_formats[image_format])
        resized_img = cv2.resize(cv_image, new_image_size)
        if image_format == 'gray':
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        yield resized_img


def save_images(dataset: pd.DataFrame, directory: str, new_image_size: tuple[int, int] = (224, 224),
                image_format: str = 'gray') -> None:
    """
    Save images png format in directory
    Path and file name: {directory}/{train|test}/{index file in dataset}_{emotion}.png

    Parameters
    ------------------------
    dataset: pd.Dataframe
    directory: str
    new_image_size: tuple[int, int], default = (224, 224)
    image_format: {'gray', 'bgr', 'rgb'},  default = 'gray'
    """
    if "/" not in directory:
        directory += "/"
    img_arr = get_pixel_array(dataset)

    dataset[" Usage"] = dataset[" Usage"].apply(lambda x: "train" if "train" in x.lower() else "test")

    for i in dataset[" Usage"].unique():
        Path(directory+i).mkdir(parents=True, exist_ok=True)

    filepath: list[str] = [directory + dataset[" Usage"][i] + "/"
                           + str(i) + "_" + str(dataset.iloc[i, 0]) + ".png"
                           for i in range(dataset.shape[0])]

    for item, image in zip(range(dataset.shape[0]), resize_images(img_arr, new_image_size, image_format)):
        cv2.imwrite(filepath[item], image)


def read_images_from_dir(directory: str) -> Iterator[tuple[int, np.ndarray]]:
    """
    Read images from directory and return emotion and image.
    """
    p = Path(directory)
    for path in p.rglob("*.png"):
        image = cv2.imread(str(path), cv2.COLOR_BGR2GRAY)
        emotion = int(path.name.split(".")[0].split("_")[1])
        yield emotion, np.asarray(image)


# save_images(pd.concat([train_dataset, test_dataset], ignore_index=True), "data")
