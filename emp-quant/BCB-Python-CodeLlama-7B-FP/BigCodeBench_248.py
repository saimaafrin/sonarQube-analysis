import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(data_list):
    """
    Unzips the provided list of tuples and plots the numerical values for each position.
    """
    if not data_list:
        raise ValueError("The data_list is empty.")

    x_values = []
    y_values = []

    for x, y in data_list:
        x_values.append(x)
        y_values.append(y)

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Unzipped Numerical Values")
    plt.show()
data_list = [(1, 2), (3, 4), (5, 6)]