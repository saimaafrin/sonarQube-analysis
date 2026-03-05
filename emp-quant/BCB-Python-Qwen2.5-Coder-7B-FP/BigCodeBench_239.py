import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = np.array([item for sublist in original for item in sublist if isinstance(item, (int, float))])
    
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
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.gaussian_kde(numeric_values)
    ax.plot(x, p(x), "k", linewidth=2)
    
    return numeric_values, stats_dict, ax