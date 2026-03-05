
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    # Create a generator object that yields tuples of (x, e^x)
    def generate_exponential_sequence(start, end, step):
        x_values = np.arange(start, end, step)
        y_values = np.exp(x_values)
        return [(x, y) for x, y in zip(x_values, y_values)]

    # Generate the sequence using the generator
    exponential_sequence = generate_exponential_sequence(range_start, range_end, step)

    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot([x for x, y in exponential_sequence], [y for x, y in exponential_sequence], 'o-')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    plt.show()

    return exponential_sequence, ax