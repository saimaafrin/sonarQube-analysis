import cv2
import matplotlib.pyplot as plt
import numpy as np
def task_func(image_path, kernel_size):
    """
    Applies a blur effect to an image using a specified kernel size, then visualizes both the original and blurred images side by side.
    The function should raise the exception for:
        FileNotFoundError: If the specified image file does not exist.
        ValueError: If kernel_size is not a positive integer.
    The function should output with:
        tuple: A tuple containing a numpy.ndarray of the blurred image, and two matplotlib.axes.Axes objects for the plots of the original and blurred images.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist.")

    # Check if kernel_size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size < 1:
        raise ValueError(f"Kernel size must be a positive integer. Got {kernel_size}.")

    # Read the image
    image = cv2.imread(image_path)

    # Apply the blur effect
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Create a figure and add two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the original and blurred images
    ax1.imshow(image)
    ax1.set_title("Original Image")
    ax2.imshow(blurred_image)
    ax2.set_title("Blurred Image")

    # Return the blurred image and the two subplots
    return blurred_image, ax1, ax2
image_path = "image.jpg"
kernel_size = 5