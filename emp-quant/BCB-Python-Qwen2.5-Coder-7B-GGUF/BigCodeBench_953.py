
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Remove duplicates while maintaining order
    mystrings = list(dict.fromkeys(mystrings))
    
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            raise FileNotFoundError(f"Cannot create directory {folder_path}: {e}")
    
    saved_files = []
    for title in mystrings:
        # Generate random data points
        data = np.random.rand(10)
        
        # Create bar chart
        plt.figure()
        plt.bar(range(10), data)
        plt.title(title)
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        
        # Save the plot
        file_name = f"{title.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()
        
        saved_files.append(file_name)
    
    return saved_files