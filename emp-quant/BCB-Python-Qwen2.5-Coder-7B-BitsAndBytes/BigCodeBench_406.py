
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file {img_path} does not exist.")
    
    # Open the image
    img = Image.open(img_path)
    
    # Convert the image to a numpy array
    img_np = np.array(img)
    
    # Rotate the image
    rotated_img = img.rotate(angle, expand=True)
    
    # Convert the rotated image to a numpy array
    rotated_img_np = np.array(rotated_img)
    
    # Display both images side by side using matplotlib
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_np)
    axs[0].set_title('Original Image')
    axs[1].imshow(rotated_img_np)
    axs[1].set_title('Rotated Image')
    plt.show()
    
    # Return both images as numpy arrays
    return (img_np, rotated_img_np)