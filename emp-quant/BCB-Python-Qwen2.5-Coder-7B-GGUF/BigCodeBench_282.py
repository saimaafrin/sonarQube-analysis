
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os

def task_func(file_path, onpick):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the image
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError(f"Failed to load the image from {file_path}.")
    
    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Reshape the image to a 2D array of pixels
    pixels = image_rgb.reshape(-1, 3)
    
    # Create a 3D histogram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges, zedges = np.histogramdd(pixels, bins=256, range=[(0, 256), (0, 256), (0, 256)])
    
    # Plot the histogram
    ax.voxels(xedges, yedges, zedges, hist, edgecolor='k')
    
    # Connect the onpick event
    fig.canvas.mpl_connect('button_press_event', onpick)
    
    return ax