import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os
def task_func(file_path, onpick):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the image
    image = cv2.imread(file_path)
    
    # Convert the image to RGB if it's in BGR format
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Flatten the image to get the RGB values
    r, g, b = image[:, :, 0].flatten(), image[:, :, 1].flatten(), image[:, :, 2].flatten()
    
    # Create a 3D histogram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(r, g, b, c='r', marker='o')
    
    # Connect the onpick event to the onpick function
    fig.canvas.mpl_connect('pick_event', onpick)
    
    return ax