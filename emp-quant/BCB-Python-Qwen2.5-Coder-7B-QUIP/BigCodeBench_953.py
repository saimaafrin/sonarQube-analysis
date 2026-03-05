
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Ensure the directory exists
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            raise FileNotFoundError(f"Failed to create directory: {e}")

    # Generate and save bar charts
    file_names = []
    for name in mystrings:
        # Generate 10 random data points in [0, 1)
        data = np.random.rand(10)

        # Create a bar chart
        plt.figure(figsize=(6, 4))
        plt.bar(range(10), data, tick_label=range(1, 11))
        plt.title(name)
        plt.xlabel('Data Point')
        plt.ylabel('Value')

        # Save the bar chart as a .png file
        file_name = f"{name.replace(' ', '_')}.png"
        plt.savefig(os.path.join(folder_path, file_name))
        plt.close()

        # Append the file name to the list
        file_names.append(file_name)

    return file_names