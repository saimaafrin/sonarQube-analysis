from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Open an image file and scale it by different scaling factors.
    Display each scaled image using matplotlib and return the scaled images with their Axes.
    """
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} not found.")

    # Read the image file
    img = Image.open(img_path)

    # Initialize the list to store the scaled images and their Axes
    scaled_images = []

    # Iterate over the scaling factors
    for scale_factor in scale_factors:
        # Resize the image
        resized_img = resize(img, (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)))

        # Convert the resized image to numpy array
        resized_img_array = np.array(resized_img)

        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Display the resized image
        ax.imshow(resized_img_array)

        # Add the scaled image and its Axes to the list
        scaled_images.append((ax, resized_img_array))

    # Return the list of scaled images and their Axes
    return scaled_images
img_path = "image.jpg"
scale_factors = [0.5, 0.75, 1.5, 2.0]