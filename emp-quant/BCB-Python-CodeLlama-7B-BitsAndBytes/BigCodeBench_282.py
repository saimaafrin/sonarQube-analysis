
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
    img = cv2.imread(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate the histogram of the image
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Create a 3D plot of the histogram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar(hist, color='blue')

    # Add a pick event to the plot
    def onpick(event):
        # Get the coordinates of the selected point
        x, y = event.artist.get_x(), event.artist.get_y()

        # Print the coordinates of the selected point
        print(f"Selected point: ({x}, {y})")

    # Add the pick event to the plot
    ax.pick_event = onpick

    # Show the plot
    plt.show()

# Call the function with the image file path
task_func("image.jpg", onpick)