
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Check if 'n_clusters' is a positive integer
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("'n_clusters' must be a positive integer")
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image file does not exist at the specified path: {image_path}")
    
    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(pixels)
    segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]
    
    # Reshape the segmented pixels back to the original image shape
    segmented_image = segmented_pixels.reshape(image.shape)
    
    return image, segmented_image