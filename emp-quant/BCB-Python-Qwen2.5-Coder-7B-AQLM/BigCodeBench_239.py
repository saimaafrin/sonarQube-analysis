
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = np.array([item for sublist in original for item in sublist if isinstance(item, (int, float))])
    
    # Compute basic statistics
    mean = np.mean(numeric_values)
    std_dev = np.std(numeric_values)
    minimum = np.min(numeric_values)
    maximum = np.max(numeric_values)
    statistics = {
        'mean': mean,
        'standard deviation': std_dev,
        'minimum': minimum,
        'maximum': maximum
    }
    
    # Generate histogram with overlaid PDF
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(numeric_values, bins='auto', density=True, alpha=0.6)
    pdf = stats.norm.pdf(bins, mean, std_dev)
    ax.plot(bins, pdf, 'k', linewidth=2)
    
    return numeric_values, statistics, ax