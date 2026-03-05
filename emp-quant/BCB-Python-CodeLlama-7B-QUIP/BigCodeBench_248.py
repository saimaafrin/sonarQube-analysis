
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    if not data_list:
        raise ValueError("Data list is empty")
    data_list = np.array(data_list)
    x = data_list[:, 0]
    y = data_list[:, 1]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Unzipped Data")
    plt.show()
    return fig