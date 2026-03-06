
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    """
    Creates a histogram of the pixel values of a grayscale image.

    Args:
        image_file (str): The path to the image file.

    Returns:
        np.ndarray: A 1D numpy array representing the histogram of the image, with 256 bins corresponding to
        the pixel values in the range [0, 256). Each entry in the array represents the frequency of a pixel value
        in the grayscale image.

    Raises:
        FileNotFoundError: If the specified image file does not exist.
        ValueError: If the image file is not a valid image.
    """
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"Image file '{image_file}' does not exist.")

    # Load the image using OpenCV
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        raise ValueError(f"Image file '{image_file}' is not a valid image.")

    # Create a histogram of the pixel values
    histogram = np.zeros(256, dtype=np.uint64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i, j]] += 1

    return histogram