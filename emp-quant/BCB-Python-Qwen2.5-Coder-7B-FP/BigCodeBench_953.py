import numpy as np
import matplotlib.pyplot as plt
import os
def task_func(mystrings, folder_path, seed=None):
    # Ensure the directory exists, create if not
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except Exception as e:
            raise FileNotFoundError(f"Cannot create directory: {folder_path}") from e

    # Initialize the list to store the names of saved files
    saved_files = []

    # Iterate over each plot name in the list
    for plot_name in mystrings:
        # Generate 10 random data points in the range [0, 1)
        data_points = np.random.rand(10)

        # Create a bar chart
        plt.figure()
        plt.bar(range(1, 11), data_points)
        plt.title(plot_name)
        plt.xlabel('Data Point Index')
        plt.ylabel('Random Value')

        # Save the bar chart as a .png file in the specified directory
        file_name = f"{plot_name.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()

        # Append the file name to the list of saved files
        saved_files.append(file_name)

    return saved_files