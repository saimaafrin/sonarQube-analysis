from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Open an image file and scale it by different scaling factors. Display each scaled image using matplotlib and return the scaled images with their Axes.

    Parameters:
    img_path (str): The path to the image file.
    scale_factors (list): A list of scaling factors to apply to the image.

    Returns:
    list of tuples: Each tuple contains (matplotlib.axes.Axes, numpy.ndarray) representing the Axes and the pixel values of the scaled image.

    Raises:
    FileNotFoundError: If the image file cannot be found.
    """
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file {img_path} does not exist.")

    # Open the image file
    with Image.open(img_path) as img:
        # Convert the image to a numpy array
        img_array = np.array(img)

        # Initialize a list to store the results
        results = []

        # Loop through the scaling factors
        for scale_factor in scale_factors:
            # Resize the image using skimage.transform.resize
            scaled_img_array = resize(img_array, (int(img_array.shape[0] * scale_factor), int(img_array.shape[1] * scale_factor)), mode='reflect')

            # Display the scaled image using matplotlib
            fig, ax = plt.subplots()
            ax.imshow(scaled_img_array, cmap='gray')
            ax.axis('off')

            # Append the Axes and the pixel values of the scaled image to the results list
            results.append((ax, scaled_img_array))

        return results