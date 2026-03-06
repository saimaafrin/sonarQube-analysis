
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Create the directory if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate random data points for each plot
    data = []
    for i, title in enumerate(mystrings):
        data.append(np.random.rand(10))

    # Create the bar charts and save them as .png files
    for i, title in enumerate(mystrings):
        fig, ax = plt.subplots()
        ax.bar(range(10), data[i])
        ax.set_title(title)
        fig.savefig(os.path.join(folder_path, f'{title}.png'))

    # Return the list of file names where the plots are saved
    return [os.path.join(folder_path, f'{title}.png') for title in mystrings]

# Call the function and save the plots
file_names = task_func(mystrings, folder_path)
print(file_names)