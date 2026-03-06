
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    # Open the image file
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        raise FileNotFoundError("Image file not found")

    # Scale the image by different scaling factors
    scaled_imgs = []
    for scale_factor in scale_factors:
        scaled_img = resize(img, (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor)))
        scaled_imgs.append(scaled_img)

    # Display each scaled image using matplotlib
    fig, axs = plt.subplots(nrows=len(scaled_imgs), ncols=1, figsize=(10, 10))
    for i, scaled_img in enumerate(scaled_imgs):
        axs[i].imshow(scaled_img)
        axs[i].set_title(f"Scaled by {scale_factors[i]}")

    # Return the scaled images with their Axes
    return [(axs[i], scaled_imgs[i]) for i in range(len(scaled_imgs))]

# Display the scaled images
for ax, scaled_img in scaled_imgs_with_axes:
    ax.set_axis_off()
    ax.imshow(scaled_img)
    ax.set_title(f"Scaled by {scale_factors[i]}")

plt.show()