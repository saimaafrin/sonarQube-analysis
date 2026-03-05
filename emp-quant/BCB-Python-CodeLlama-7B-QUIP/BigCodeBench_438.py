
import pickle
import os
import matplotlib.pyplot as plt

def task_func(numbers, file_path="save.pkl"):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    fig, ax = plt.subplots()
    ax.hist(numbers, bins=50)
    fig.savefig(file_path)
    loaded_fig = plt.figure(file_path)
    os.remove(file_path)
    return loaded_fig