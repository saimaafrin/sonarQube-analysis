import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
def task_func(image, sigma=2):
    """
    Apply a Gaussian filter to a given image and draw the original and filtered images side by side.
    The function should raise the exception for:
        ValueError: If sigma is non-positive.
        TypeError: If the input is not a numpy array.
    The function should output with:
        ax (matplotlib.axes.Axes): Axes object containing the plot. Two plots with titles 'Original' and 'Filtered'.
        filtered_image (numpy.ndarray): The numpy array of pixel values for the filtered image.
    """
    if sigma <= 0:
        raise ValueError("Sigma must be positive.")
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")

    # Apply the Gaussian filter
    filtered_image = gaussian_filter(image, sigma)

    # Create a figure and axis object
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the original and filtered images
    ax[0].imshow(image, cmap="gray")
    ax[0].set_title("Original")
    ax[1].imshow(filtered_image, cmap="gray")
    ax[1].set_title("Filtered")

    return ax, filtered_image
image = np.random.rand(100, 100)