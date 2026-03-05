import cv2
import os
from matplotlib import pyplot as plt
def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file {image_path} does not exist.")
    
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was successfully read
    if image is None:
        raise ValueError(f"Failed to read the image file {image_path}.")
    
    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Normalize the histogram
    cv2.normalize(histogram, histogram, 0, 255, cv2.NORM_MINMAX)
    
    # Convert the histogram to an 8-bit image
    histogram = cv2.normalize(histogram, None, 0, 255, cv2.NORM_MINMAX).astype("uint8")
    
    # Create a figure and axis for the histogram plot
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.plot(histogram, color='gray')
    
    # Set the title and labels
    ax.set_title('Histogram of Image Pixel Intensities')
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')
    
    # Display the original image
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    
    # Save the histogram as a PNG file
    plt.savefig(histogram_path)
    
    # Return the histogram plot object
    return ax