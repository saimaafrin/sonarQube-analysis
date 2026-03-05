from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Scales an image by different factors and displays each scaled image using matplotlib.
    
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
        
        # Loop through each scaling factor
        for scale in scale_factors:
            # Calculate the new size of the image
            new_size = (int(img.width * scale), int(img.height * scale))
            
            # Resize the image using skimage.transform.resize
            scaled_img_array = resize(img_array, new_size, anti_aliasing=True)
            
            # Convert the scaled image back to a PIL image
            scaled_img = Image.fromarray((scaled_img_array * 255).astype(np.uint8))
            
            # Display the scaled image using matplotlib
            fig, ax = plt.subplots()
            ax.imshow(scaled_img)
            ax.axis('off')
            
            # Append the Axes and the pixel values of the scaled image to the results list
            results.append((ax, scaled_img_array))
    
    return results