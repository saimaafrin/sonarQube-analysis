import numpy as np
import matplotlib.pyplot as plt
import os
def task_func(mystrings, folder_path, seed=None):
    """
    Generates random data points to plot bar charts for each in a given list of plot names, then saves them in a specified directory.
    This function takes a list of plot names, for each generating 10 random data points in [0, 1) to create a bar chart, then saves the bar charts as .png files in the specified directory, creating the directory if it does not exist.
    """
    # Check if the directory path exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate random data points for each plot
    data = []
    for plot_name in mystrings:
        data.append(np.random.uniform(0, 1, size=10))

    # Create a bar chart for each plot
    for i, plot_name in enumerate(mystrings):
        plt.bar(range(10), data[i], label=plot_name)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(plot_name)
        plt.legend()
        plt.savefig(os.path.join(folder_path, f'{plot_name}.png'))
        plt.close()

    # Return the list of file names where the plots are saved
    return [os.path.join(folder_path, f'{plot_name}.png') for plot_name in mystrings]
mystrings = ['First Plot', 'Second Plot']
folder_path = './another_folder/'