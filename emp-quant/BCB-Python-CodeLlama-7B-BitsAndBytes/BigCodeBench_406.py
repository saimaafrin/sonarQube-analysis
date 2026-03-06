
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Open the image and convert it to a numpy array
    img = Image.open(img_path)
    img_array = np.array(img)

    # Rotate the image by the specified angle
    rotated_img = img.rotate(angle, expand=True)
    rotated_img_array = np.array(rotated_img)

    # Display both images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
    ax1.imshow(img_array, cmap='gray')
    ax2.imshow(rotated_img_array, cmap='gray')
    plt.show()

    # Return both images as numpy arrays
    return img_array, rotated_img_array

try:
    img_array, rotated_img_array = task_func(img_path, angle)
except FileNotFoundError as e:
    print(e)
else:
    print("Images displayed side by side")