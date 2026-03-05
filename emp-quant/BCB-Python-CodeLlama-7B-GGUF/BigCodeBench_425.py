
import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Read the image
    image = cv2.imread(image_path)

    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Normalize the histogram
    histogram = histogram.astype("float")
    histogram /= histogram.sum()

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(histogram.index, histogram.values, width=1)
    ax.set_xlabel("Pixel intensity")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of image pixel intensities")

    # Save the histogram as a PNG file
    fig.savefig(histogram_path)

    # Return the histogram plot object
    return ax