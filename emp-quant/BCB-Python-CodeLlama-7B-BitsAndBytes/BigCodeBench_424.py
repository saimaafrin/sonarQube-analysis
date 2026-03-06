
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Load the image and convert it to RGB
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Check if 'n_clusters' is a positive integer
    if n_clusters <= 0:
        raise ValueError(f"'n_clusters' must be a positive integer, not {n_clusters}")

    # Apply K-means clustering to segment the image
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(image.reshape(-1, 3))
    segmented_image = kmeans.cluster_centers_[kmeans.labels_]

    # Save the segmented image as a separate file
    segmented_image_path = os.path.splitext(image_path)[0] + '_segmented.jpg'
    cv2.imwrite(segmented_image_path, segmented_image)

    # Return the original and segmented images as numpy arrays
    return image, segmented_image