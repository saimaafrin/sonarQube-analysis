import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(range_start=0, range_end=10, step=0.1):
    # Create a generator object that yields tuples of (x, e^x)
    def exponential_generator():
        x = range_start
        while x <= range_end:
            yield (x, math.exp(x))
            x += step

    # Generate the sequence of tuples using the generator
    exponential_sequence = list(exponential_generator())

    # Plot the exponential function using the generated values
    x_values, y_values = zip(*exponential_sequence)
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('e^x')
    plt.title('Exponential Function')
    plt.grid(True)
    plt.show()

    # Return the generator object and the plotted Axes object
    return exponential_generator(), plt.gca()