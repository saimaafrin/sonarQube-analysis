
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found: {img_path}")
    
    original_img = Image.open(img_path)
    original_img = np.array(original_img)
    
    scaled_images = []
    
    for factor in scale_factors:
        scaled_img = resize(original_img, (int(original_img.shape[0] * factor), int(original_img.shape[1] * factor)), mode='bilinear')
        scaled_img = Image.fromarray(scaled_img)
        
        fig, ax = plt.subplots()
        ax.imshow(scaled_img, interpolation='nearest')
        ax.axis('off')
        
        scaled_images.append((ax, scaled_img))
    
    return scaled_images