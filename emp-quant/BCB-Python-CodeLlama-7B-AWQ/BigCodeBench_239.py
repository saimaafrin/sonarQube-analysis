import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = [value for value in original if isinstance(value, (int, float))]

    # Compute basic statistics for the numeric values
    mean = np.mean(numeric_values)
    std = np.std(numeric_values)
    min_value = np.min(numeric_values)
    max_value = np.max(numeric_values)

    # Generate a histogram with an overlaid probability density function (PDF)
    fig, ax = plt.subplots()
    ax.hist(numeric_values, density=True, alpha=0.6, bins='auto')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram with Overlaid PDF')
    ax.set_xlim([min_value, max_value])
    ax.set_ylim([0, 1])
    ax.grid(True)

    # Return the numpy array of extracted numeric values, basic statistics, and the matplotlib Axes object
    return np.array(numeric_values), {'mean': mean, 'std': std, 'min': min_value, 'max': max_value}, ax
original = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]