
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    try:
        # Open the image file
        img = Image.open(img_path)
        img_np = np.array(img)
        
        # Initialize a list to store the results
        results = []
        
        # Loop through each scale factor
        for scale in scale_factors:
            # Resize the image
            scaled_img = resize(img_np, (int(img_np.shape[0] * scale), int(img_np.shape[1] * scale)), anti_aliasing=True)
            
            # Create a new figure and axes for each scaled image
            fig, ax = plt.subplots()
            ax.imshow(scaled_img)
            ax.axis('off')
            
            # Append the axes and the scaled image to the results list
            results.append((ax, scaled_img))
        
        return results
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The image file at {img_path} could not be found.")