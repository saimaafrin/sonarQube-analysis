
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    try:
        # Open the image file
        img = Image.open(img_path)
        
        # Convert the image to a numpy array
        img_array = np.array(img)
        
        # Initialize a list to store the results
        results = []
        
        # Loop through each scale factor
        for scale_factor in scale_factors:
            # Resize the image using the given scale factor
            scaled_img_array = resize(img_array, (int(img.height * scale_factor), int(img.width * scale_factor)), anti_aliasing=True)
            
            # Create a new figure and axis for displaying the scaled image
            fig, ax = plt.subplots()
            
            # Display the scaled image on the axis
            ax.imshow(scaled_img_array)
            
            # Append the axis and the scaled image array to the results list
            results.append((ax, scaled_img_array))
        
        return results
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The image file '{img_path}' could not be found.")