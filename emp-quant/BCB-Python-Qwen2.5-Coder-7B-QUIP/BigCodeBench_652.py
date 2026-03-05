
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
def task_func(target_value=TARGET_VALUE, array=ARRAY):
    # Find row indices where the first cell matches the target value
    matching_indices = np.where(array[0] == target_value)[0]
    
    # Check if any matching indices were found
    if matching_indices.size == 0:
        return 'N/A'
    
    # Perform statistical analysis
    mean = np.mean(matching_indices)
    variance = np.var(matching_indices)
    skewness = stats.skew(matching_indices)
    kurtosis = stats.kurtosis(matching_indices)
    
    # Plot the distribution of the indices
    plt.hist(matching_indices, bins='auto', edgecolor='k')
    plt.title('Distribution of Matching Indices')
    plt.xlabel('Index')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the statistical analysis results
    return (mean, variance, skewness, kurtosis)