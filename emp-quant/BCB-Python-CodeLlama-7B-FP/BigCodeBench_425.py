import cv2
import os
from matplotlib import pyplot as plt
def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    """
    Read an image, create a histogram of the image pixel intensities, save the histogram as a PNG file, and return the histogram plot object.
    The function also displays the original image and its histogram.
    The limit to the size of the image depends on the hardware capabilities of the system you are working on.
    A possible size of an image is 20x20.
    The function should raise the exception for:
        FileNotFoundError: If the image file does not exist at the specified path.
    The function should output with:
        matplotlib.axes.Axes: The Axes object of the histogram plot.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Read the image
    image = cv2.imread(image_path)

    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist(image, [0], None, [256], [0, 256])

    # Normalize the histogram
    histogram = histogram / histogram.max()

    # Create a figure and axis for the histogram
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(histogram.index, histogram.values, width=1, color='blue')

    # Set the title and labels
    ax.set_title("Histogram of Image Pixel Intensities")
    ax.set_xlabel("Pixel Intensity")
    ax.set_ylabel("Frequency")

    # Save the histogram as a PNG file
    fig.savefig(histogram_path)

    # Return the histogram plot object
    return ax
image_path = "image.jpg"
histogram_path = "histogram.png"