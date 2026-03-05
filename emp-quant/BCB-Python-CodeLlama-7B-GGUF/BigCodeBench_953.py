
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        raise FileNotFoundError("The provided directory path does not exist and cannot be created.")

    for i, title in enumerate(mystrings):
        data = np.random.uniform(0, 1, size=10)
        plt.bar(range(10), data)
        plt.title(title)
        plt.savefig(os.path.join(folder_path, f"{title}.png"))
        plt.close()

    return [os.path.join(folder_path, f"{title}.png") for title in mystrings]