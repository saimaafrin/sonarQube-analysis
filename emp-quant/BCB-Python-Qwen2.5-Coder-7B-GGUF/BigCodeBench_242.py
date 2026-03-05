
import cv2
import matplotlib.pyplot as plt

def task_func(image_path, kernel_size):
    # Check if the image file exists
    if not cv2.imread(image_path):
        raise FileNotFoundError("The specified image file does not exist.")
    
    # Check if kernel_size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size <= 0:
        raise ValueError("kernel_size must be a positive integer.")
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply the blur effect
    blurred_image = cv2.GaussianBlur(image_rgb, (kernel_size, kernel_size), 0)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display the original image
    axes[0].imshow(image_rgb)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Display the blurred image
    axes[1].imshow(blurred_image)
    axes[1].set_title('Blurred Image')
    axes[1].axis('off')
    
    # Return the blurred image and the two axes objects
    return blurred_image, axes[0], axes[1]