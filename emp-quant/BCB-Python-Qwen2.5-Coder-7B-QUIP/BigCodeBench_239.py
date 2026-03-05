
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = np.array([item[1] for item in original])

    # Compute basic statistics
    stats_dict = {
        'mean': np.mean(numeric_values),
        'std_dev': np.std(numeric_values),
        'min': np.min(numeric_values),
        'max': np.max(numeric_values)
    }

    # Generate histogram with overlaid PDF
    fig, ax = plt.subplots()
    ax.hist(numeric_values, density=True, alpha=0.6, bins='auto')
    ax.plot(numeric_values, stats.norm.pdf(numeric_values, np.mean(numeric_values), np.std(numeric_values)), 'r')

    return numeric_values, stats_dict, ax