
import cv2
import matplotlib.pyplot as plt

def task_func(image_path, kernel_size):
    # Check if the kernel_size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size <= 0:
        raise ValueError("kernel_size must be a positive integer")
    
    # Read the image from the given path
    try:
        image = cv2.imread(image_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The image at {image_path} could not be found.")
    
    # Apply Gaussian Blur to the image
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Create a figure to display the images
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Display the blurred image
    axes[1].imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Blurred Image')
    axes[1].axis('off')
    
    # Return the blurred image and the axes objects
    return blurred_image, axes[0], axes[1]