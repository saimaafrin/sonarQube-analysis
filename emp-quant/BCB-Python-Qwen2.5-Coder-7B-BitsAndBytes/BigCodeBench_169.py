
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def task_func(image, sigma=2):
    """
    Apply a Gaussian filter to a given image and draw the original and filtered images side by side.

    Parameters:
    - image (numpy.ndarray): Input image as a numpy array.
    - sigma (float): Standard deviation for Gaussian kernel. Must be positive.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object containing the plot.
    - filtered_image (numpy.ndarray): The numpy array of pixel values for the filtered image.
    """

    # Check if sigma is non-positive
    if sigma <= 0:
        raise ValueError("Sigma must be positive.")

    # Check if the input is not a numpy array
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")

    # Apply Gaussian filter
    filtered_image = gaussian_filter(image, sigma=sigma)

    # Create a figure and axis
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Display the original image
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original')

    # Display the filtered image
    ax[1].imshow(filtered_image, cmap='gray')
    ax[1].set_title('Filtered')

    # Show the plot
    plt.show()

    return ax, filtered_image