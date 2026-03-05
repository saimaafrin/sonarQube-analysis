import numpy as np
import matplotlib.pyplot as plt
import os
def task_func(mystrings, folder_path, seed=None):
    """
    Generates random data points to plot bar charts for each in a given list of plot names, then saves them in a specified directory.

    Parameters
    ----------
    mystrings : list
        List of plot names.
    folder_path : str
        Path to the directory where the bar charts will be saved.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    list
        Names of the files where the plots are saved. Each file corresponds to a title from `mystrings`.

    Raises
    ------
    FileNotFoundError
        If the provided directory path does not exist and cannot be created.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if seed is not None:
        np.random.seed(seed)
    data = []
    for title in mystrings:
        data.append(np.random.rand(10))
    for i, title in enumerate(mystrings):
        plt.bar(range(10), data[i], label=title)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(title)
        plt.legend()
        plt.savefig(os.path.join(folder_path, f'{title}.png'))
        plt.close()
    return [os.path.join(folder_path, f'{title}.png') for title in mystrings]
mystrings = ['First Plot', 'Second Plot']
folder_path = './another_folder/'
seed = 42