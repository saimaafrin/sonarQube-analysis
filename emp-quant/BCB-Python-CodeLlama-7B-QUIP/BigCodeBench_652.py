
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
def task_func(target_value=TARGET_VALUE, array=ARRAY):
    # Find the indices of the target value in the array
    target_indices = np.where(array == target_value)
    # Check if the target value was found in the array
    if len(target_indices) == 0:
        return 'N/A'
    # Perform statistical analysis on the indices
    mean = stats.mean(target_indices)
    variance = stats.var(target_indices)
    skewness = stats.skewness(target_indices)
    kurtosis = stats.kurtosis(target_indices)
    # Plot the distribution of the indices
    plt.hist(target_indices, bins=50)
    plt.show()
    return (mean, variance, skewness, kurtosis)