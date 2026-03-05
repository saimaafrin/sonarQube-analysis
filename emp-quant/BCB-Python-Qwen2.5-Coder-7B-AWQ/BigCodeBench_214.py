import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
def task_func(seed=42, image_size=(100, 100, 3), range_low=0, range_high=255):
    """
    Generate a random RGB image and view it.

    Parameters:
    - seed (int): Seed for random number generation.
    - image_size (tuple): Size of the image (height, width, channels).
    - range_low (int): Lower bound for the range of RGB values.
    - range_high (int): Upper bound for the range of RGB values.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object of the plot.
    - image (numpy.ndarray): The numpy array of the generated image.

    Raises:
    - ValueError: If range_low is not less than range_high.
    """
    if range_low >= range_high:
        raise ValueError("range_low must be less than range_high")

    random.seed(seed)
    image = np.random.randint(range_low, range_high, size=image_size, dtype=np.uint8)
    ax = plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    return ax, image