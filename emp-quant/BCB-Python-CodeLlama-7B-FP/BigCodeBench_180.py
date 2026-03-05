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

    # Load the image
    img = Image.open(img_path)

    # Scale the image
    scaled_images = []
    for scale_factor in scale_factors:
        scaled_img = resize(img, (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)))
        scaled_images.append(scaled_img)

    # Display each scaled image using matplotlib
    fig, axs = plt.subplots(len(scaled_images), 1, figsize=(10, 10))
    for i, scaled_img in enumerate(scaled_images):
        axs[i].imshow(scaled_img)
        axs[i].set_title(f"Scaled by {scale_factors[i]}")

    # Return the scaled images with their Axes
    return [(axs[i], scaled_images[i]) for i in range(len(scaled_images))]
img_path = "image.jpg"
scale_factors = [0.5, 0.75, 1.5, 2.0]