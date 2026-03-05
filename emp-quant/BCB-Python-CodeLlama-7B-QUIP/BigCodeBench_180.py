
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    # Load the image file
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file {img_path} not found")

    # Create a list to store the scaled images and their corresponding axes
    scaled_images = []

    # Loop over the scaling factors and apply them to the image
    for scale_factor in scale_factors:
        # Resize the image using the scaling factor
        scaled_img = resize(img, scale_factor)

        # Convert the image to a numpy array
        img_array = np.array(scaled_img)

        # Display the scaled image using matplotlib
        fig, ax = plt.subplots()
        ax.imshow(img_array, cmap="gray")
        ax.set_title(f"Scaled image with scale factor {scale_factor}")
        scaled_images.append((ax, img_array))

    return scaled_images