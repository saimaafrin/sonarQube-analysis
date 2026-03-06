
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = [item[1] for item in original]
    
    # Convert the list to a numpy array
    numeric_array = np.array(numeric_values)
    
    # Compute basic statistics
    mean_value = np.mean(numeric_array)
    std_deviation = np.std(numeric_array)
    min_value = np.min(numeric_array)
    max_value = np.max(numeric_array)
    
    statistics = {
        'mean': mean_value,
        'standard deviation': std_deviation,
        'minimum': min_value,
        'maximum': max_value
    }
    
    # Generate a histogram with overlaid PDF
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(numeric_array, density=True, alpha=0.6, bins='auto')
    fit = stats.norm.pdf(bins, mean_value, std_deviation)
    ax.plot(bins, fit, 'k--', linewidth=2)
    
    return numeric_array, statistics, ax