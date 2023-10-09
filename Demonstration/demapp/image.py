from PIL import Image
import pandas as pd
import numpy as np
import numpy.typing as npt

SIZEIMG = (224, 224)

train_dataset = pd.read_csv("train.csv")
test_dataset = pd.read_csv("test.csv")


def get_img_dataset(dataset=train_dataset) -> npt.DTypeLike:
    img_arr = dataset[' pixels'].copy()
    for i in range(len(img_arr)):
        img_arr[i] = np.fromstring(img_arr[i], dtype=np.uint8, sep=' ')
        img_arr[i] = np.reshape(img_arr[i], (48, 48))
    return np.stack(img_arr.to_numpy())


images_arr = get_img_dataset(train_dataset)
