
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os

def task_func(file_path, onpick):
    # Check if the image file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Image file does not exist")

    # Load the image using OpenCV
    image = cv2.imread(file_path)

    # Create a figure and axis
    fig = plt.figure()
    ax = fig.add_axes(projection='3d')

    # Create a histogram of the image
    hist = np.histogram(image.flatten(), bins=256, range=(0, 256))

    # Set the histogram as the data for the 3D plot
    ax.hist(hist, bins=256, range=(0, 256))

    # Set the title and labels
    ax.set_title("Color Histogram")
    ax.set_xlabel("Red")
    ax.set_ylabel("Green")
    ax.set_zlabel("Blue")

    # Set the callback function to be called when a data point is selected
    ax.callbacks.connect('pick_event', onpick)

    # Show the figure
    plt.show()

# Define the callback function
def onpick(event):
    # Get the x and y coordinates of the selected data point
    x = event.x
    y = event.y

    # Print the coordinates
    print(f"Selected data point: ({x}, {y})")

# Call the function
task_func("image.jpg", onpick)