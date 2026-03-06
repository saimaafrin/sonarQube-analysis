
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

def task_func(seed=42, image_size=(100, 100, 3), range_low=0, range_high=255):
    """
    Generates a random RGB image and displays it.

    Parameters:
    seed (int): Seed for random number generation.
    image_size (tuple): Size of the image (height, width, channels).
    range_low (int): Lower bound for the pixel values.
    range_high (int): Upper bound for the pixel values.

    Returns:
    ax (matplotlib.axes.Axes): Axes object of the plot.
    image (numpy.ndarray): The numpy array of the generated image.
    """
    if range_low >= range_high:
        raise ValueError("range_low must be less than range_high")

    # Set the seed for reproducibility
    random.seed(seed)

    # Generate a random image
    image = np.random.randint(range_low, range_high, size=image_size, dtype=np.uint8)

    # Display the image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')  # Turn off axis numbers and ticks

    return ax, image