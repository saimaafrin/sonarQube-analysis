import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = [value for value in original if isinstance(value, (int, float))]

    # Compute basic statistics for the array
    mean = np.mean(numeric_values)
    std = np.std(numeric_values)
    min = np.min(numeric_values)
    max = np.max(numeric_values)

    # Generate a histogram with an overlaid probability density function (PDF)
    fig, ax = plt.subplots()
    ax.hist(numeric_values, density=True, alpha=0.6, bins='auto')
    ax.plot(stats.norm.pdf(numeric_values, mean, std), color='red')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram with overlaid PDF')
    plt.show()

    # Return the numpy array of extracted numeric values, basic statistics, and the matplotlib Axes object
    return np.array(numeric_values), {'mean': mean, 'std': std, 'min': min, 'max': max}, ax
original = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]