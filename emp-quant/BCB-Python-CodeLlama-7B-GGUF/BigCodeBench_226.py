
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    # Generate a sequence of tuples containing x and e^x values
    x_values = np.arange(range_start, range_end, step)
    e_values = np.exp(x_values)
    tuples = zip(x_values, e_values)

    # Plot the exponential function using the generated values
    fig, ax = plt.subplots()
    ax.plot(x_values, e_values)
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    plt.show()

    return tuples, fig