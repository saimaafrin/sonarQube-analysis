import numpy as np
import matplotlib.pyplot as plt
import os
def task_func(mystrings, folder_path, seed=None):
    """
    Generates random data points to plot bar charts for each in a given list of plot names, then saves them in a specified directory.

    Parameters
    ----------
    mystrings : list of str
        List of plot names.
    folder_path : str
        Path to the directory where the plots will be saved.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    list of str
        Names of the files where the plots are saved. Each file corresponds to a title from `mystrings`.

    Raises
    ------
    FileNotFoundError
        If the provided directory path does not exist and cannot be created.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate random data points for each plot
    data = []
    for i, title in enumerate(mystrings):
        data.append(np.random.uniform(0, 1, size=10))

    # Create bar charts and save them as .png files
    for i, title in enumerate(mystrings):
        fig, ax = plt.subplots()
        ax.bar(range(10), data[i])
        ax.set_title(title)
        fig.savefig(os.path.join(folder_path, f"{title}.png"))

    # Return list of file names
    return [os.path.join(folder_path, f"{title}.png") for title in mystrings]