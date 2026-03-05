
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

def task_func(seed=42, image_size=(100, 100, 3), range_low=0, range_high=255):
    """
    Generate a random RGB image and view it.
    """
    if range_low >= range_high:
        raise ValueError("range_low must be less than range_high")

    # Set the random seed for reproducibility
    random.seed(seed)

    # Generate the random image
    image = np.random.rand(image_size[0], image_size[1], 3) * range_high

    # Convert to RGB
    image = image.astype(np.uint8)

    # Display the image
    ax = plt.axes(projection="3d")
    ax.imshow(image, cmap="gray")
    plt.show()

    return ax, image