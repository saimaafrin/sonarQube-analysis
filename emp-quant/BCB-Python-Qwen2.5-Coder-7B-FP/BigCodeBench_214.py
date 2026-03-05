import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
def task_func(seed=42, image_size=(100, 100, 3), range_low=0, range_high=255):
    """
    Generates a random RGB image and displays it using matplotlib.

    Parameters:
    - seed (int): Seed for random number generation.
    - image_size (tuple): Size of the image (height, width, channels).
    - range_low (int): Lower bound for the random values (inclusive).
    - range_high (int): Upper bound for the random values (exclusive).

    Returns:
    - ax (matplotlib.axes.Axes): Axes object of the plot.
    - image (numpy.ndarray): The numpy array of the generated image.

    Raises:
    - ValueError: If range_low is not less than range_high.
    """
    # Check if range_low is less than range_high
    if range_low >= range_high:
        raise ValueError("range_low must be less than range_high")

    # Set the random seed
    random.seed(seed)

    # Generate a random image
    image = np.random.randint(range_low, range_high, size=image_size, dtype=np.uint8)

    # Display the image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax.axis('off')  # Turn off axis numbers and ticks

    return ax, image