
import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was read successfully
    if image is None:
        raise ValueError(f"Failed to read the image file '{image_path}'.")
    
    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Display the original image
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    # Display the histogram
    plt.subplot(1, 2, 2)
    plt.plot(histogram, color='gray')
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    # Save the histogram as a PNG file
    plt.savefig(histogram_path)
    
    # Return the histogram plot object
    return plt.gca()