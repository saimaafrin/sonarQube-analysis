import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
def task_func(target_value=TARGET_VALUE, array=ARRAY):
    """
    Finds the row indices in a numpy array where the first cell matches target_value "332".
    Performs statistical analysis on these indices and plots their distribution.
    Returns a tuple with mean, variance, skewness, and kurtosis of the indices, or
    'N/A' if statistical analysis cannot be performed.
    """
    # Find the row indices where the first cell matches the target value
    indices = np.where(array[:, 0] == target_value)[0]

    # Check if any indices were found
    if len(indices) == 0:
        return 'N/A'

    # Perform statistical analysis on the indices
    mean = np.mean(indices)
    variance = np.var(indices)
    skewness = stats.skew(indices)
    kurtosis = stats.kurtosis(indices)

    # Plot the distribution of the indices
    plt.hist(indices, bins=10)
    plt.xlabel('Indices')
    plt.ylabel('Frequency')
    plt.title('Distribution of Indices')
    plt.show()

    # Return the statistical analysis results
    return (mean, variance, skewness, kurtosis)