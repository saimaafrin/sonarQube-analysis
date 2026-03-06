
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    # Create a generator object that yields tuples of (x, e^x)
    def exp_generator(start, end, step):
        x = start
        while x <= end:
            yield (x, math.exp(x))
            x += step
    
    gen = exp_generator(range_start, range_end, step)
    
    # Extract x and y values from the generator
    x_values = [next(gen)[0] for _ in range(int((range_end - range_start) / step) + 1)]
    y_values = [next(gen)[1] for _ in range(int((range_end - range_start) / step) + 1)]
    
    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='e^x')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    ax.legend()
    
    return gen, ax