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
        except Exception as e:
            raise FileNotFoundError(f"Cannot create directory: {folder_path}") from e
    
    # List to store the names of the saved files
    saved_files = []
    
    # Set the seed for reproducibility if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Generate bar charts and save them
    for plot_name in mystrings:
        # Generate 10 random data points
        data = np.random.rand(10)
        
        # Create a bar chart
        plt.figure()
        plt.bar(range(1, 11), data)
        plt.title(plot_name)
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        
        # Save the bar chart as a PNG file
        file_name = f"{plot_name.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()
        
        # Append the file name to the list
        saved_files.append(file_name)
    
    return saved_files