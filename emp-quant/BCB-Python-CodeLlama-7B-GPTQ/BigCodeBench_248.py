import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(data_list):
    """
    Unzips the provided list of tuples and plots the numerical values for each position.
    """
    if not data_list:
        raise ValueError("The data_list is empty.")

    # Unzip the data_list
    x_values = [x for x, _ in data_list]
    y_values = [y for _, y in data_list]

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Unzipped Data")
    plt.show()
data_list = [(1, 2), (3, 4), (5, 6)]