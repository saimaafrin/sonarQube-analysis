
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Ensure the directory exists
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except Exception as e:
            raise FileNotFoundError(f"Cannot create directory {folder_path}: {e}")
    
    saved_files = []
    for name in mystrings:
        # Generate random data points
        data_points = np.random.rand(10)
        
        # Create a bar chart
        plt.figure()
        plt.bar(range(10), data_points)
        plt.title(name)
        plt.xlabel('Data Point Index')
        plt.ylabel('Random Value')
        
        # Save the bar chart as a PNG file
        file_name = f"{name.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()
        
        saved_files.append(file_name)
    
    return saved_files