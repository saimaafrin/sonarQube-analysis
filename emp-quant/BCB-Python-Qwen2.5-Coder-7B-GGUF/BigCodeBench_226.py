
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
    
    # Generate the sequence of tuples
    exponential_sequence = list(exponential_generator())
    
    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot([point[0] for point in exponential_sequence], [point[1] for point in exponential_sequence], label='e^x')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    ax.legend()
    
    return exponential_sequence, ax