
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    """
    Creates a histogram of the pixel values of a grayscale image.

    Parameters:
    image_file (str): Path to the image file.

    Returns:
    np.ndarray: A 1D numpy array representing the histogram of the image, with 256 bins corresponding to
    the pixel values in the range [0, 256). Each entry in the array represents the frequency of a pixel value
    in the grayscale image.
    """
    if not os.path.isfile(image_file):
        raise FileNotFoundError(f"Image file {image_file} does not exist.")

    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image file {image_file} is not a valid image.")

    histogram = np.zeros(256, dtype=np.uint64)
    for pixel_value in image.ravel():
        histogram[pixel_value] += 1

    return histogram