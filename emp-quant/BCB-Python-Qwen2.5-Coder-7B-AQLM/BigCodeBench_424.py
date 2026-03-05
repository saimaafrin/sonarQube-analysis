
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if n_clusters is a positive integer
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer")
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError("The image file does not exist at the specified path")
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("The image file does not exist at the specified path")
    
    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    labels = kmeans.fit_predict(pixels)
    centroids = kmeans.cluster_centers_
    
    # Replace each pixel with the centroid of its cluster
    segmented_pixels = centroids[labels]
    
    # Reshape the segmented pixels back to the original image shape
    segmented_image = segmented_pixels.reshape(image.shape)
    
    # Convert the segmented image from BGR to RGB
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)
    
    return image, segmented_image