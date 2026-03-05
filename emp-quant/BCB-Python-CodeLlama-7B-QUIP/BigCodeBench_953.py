
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate random data points for each plot
    data = [np.random.rand(10) for _ in mystrings]

    # Create bar charts for each plot
    for i, plot in enumerate(mystrings):
        plt.bar(data[i])
        plt.title(plot)
        plt.savefig(os.path.join(folder_path, f"{plot}.png"))

    # Return the list of file names where the plots are saved
    return [os.path.join(folder_path, f"{plot}.png") for plot in mystrings]