
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum values of each row
    max_values = np.max(matrix, axis=1)
    
    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(max_values, bins='auto', density=True, alpha=0.6, color='g')
    
    # Return the skewness, kurtosis, and the histogram plot
    return skewness, kurtosis, ax

    # Call the function
    skew, kurt, hist_ax = task_func(matrix)
    
    # Print the results
    print(f"Skewness: {skew}")
    print(f"Kurtosis: {kurt}")
    
    # Show the histogram plot
    plt.show()