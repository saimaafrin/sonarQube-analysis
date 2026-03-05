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
        raise FileNotFoundError(f"Image file {img_path} not found")

    # Load the image using PIL
    img = Image.open(img_path)

    # Create a list to store the scaled images and their Axes
    scaled_images = []

    # Iterate over the scaling factors
    for scale_factor in scale_factors:
        # Resize the image using scikit-image
        scaled_img = resize(img, (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)))

        # Convert the scaled image to numpy array
        scaled_img_array = np.array(scaled_img)

        # Display the scaled image using matplotlib
        fig, ax = plt.subplots()
        ax.imshow(scaled_img_array)
        ax.set_title(f"Scaled image by {scale_factor}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        # Add the scaled image and its Axes to the list
        scaled_images.append((ax, scaled_img_array))

    # Return the list of scaled images and their Axes
    return scaled_images
img_path = "image.jpg"
scale_factors = [0.5, 0.75, 1.5, 2.0]