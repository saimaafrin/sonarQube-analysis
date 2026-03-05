
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Open the image file
    img = Image.open(img_path)

    # Create a list to store the scaled images and their Axes
    scaled_images = []

    # Loop through the scaling factors
    for scale_factor in scale_factors:
        # Resize the image using the scale factor
        scaled_img = resize(img, (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)))

        # Convert the scaled image to numpy array
        scaled_img_array = np.array(scaled_img)

        # Create a new Axes object for the scaled image
        fig, ax = plt.subplots()

        # Display the scaled image on the Axes
        ax.imshow(scaled_img_array)

        # Add the Axes and the scaled image to the list
        scaled_images.append((ax, scaled_img_array))

    # Return the list of tuples
    return scaled_images