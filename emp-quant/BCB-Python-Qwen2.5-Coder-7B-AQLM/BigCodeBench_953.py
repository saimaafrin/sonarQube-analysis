
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Ensure the directory exists
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            raise FileNotFoundError(f"Failed to create directory: {folder_path}") from e

    # Initialize the random seed if provided
    if seed is not None:
        np.random.seed(seed)

    # List to store the names of the saved files
    saved_files = []

    # Process each plot name
    for plot_name in mystrings:
        # Generate 10 random data points in [0, 1)
        data_points = np.random.rand(10)

        # Create the plot
        plt.figure()
        plt.bar(range(10), data_points)
        plt.title(plot_name)
        plt.xlabel('Data Point Index')
        plt.ylabel('Random Value')

        # Save the plot as a PNG file
        file_name = f"{plot_name.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()

        # Add the file name to the list
        saved_files.append(file_path)

    return saved_files