
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def task_func(L):
    # Calculate mean
    mean = np.mean(L)
    
    # Calculate median
    median = np.median(L)
    
    # Calculate mode
    data_counts = Counter(L)
    max_count = max(list(data_counts.values()))
    mode = [num for num, count in data_counts.items() if count == max_count]
    
    # Calculate standard deviation
    std_dev = np.std(L)
    
    # Create histogram plot
    fig, ax = plt.subplots()
    ax.hist(L, bins='auto', color='blue', alpha=0.7)
    ax.set_title('Histogram of L')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    
    # Return dictionary with results and plot
    result = {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev,
        'plot': ax
    }
    return result