
import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Read the image
    image = cv2.imread(image_path)

    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist(image, [0], None, [256], [0, 256])

    # Normalize the histogram
    histogram = histogram / histogram.max()

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.plot(histogram)

    # Set the title and labels
    ax.set_title('Histogram of Image Pixel Intensities')
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')

    # Save the histogram as a PNG file
    fig.savefig(histogram_path)

    # Return the histogram plot object
    return ax

# Call the function
ax = task_func(image_path, histogram_path)

# Display the original image and its histogram
cv2.imshow('Original Image', image)
cv2.imshow('Histogram', ax)
cv2.waitKey(0)
cv2.destroyAllWindows()