import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
def task_func(target_value=TARGET_VALUE, array=ARRAY):
    # Find the row indices where the first cell matches the target value
    matching_indices = np.where(array[:, 0] == target_value)[0]
    
    # Check if any matching indices were found
    if len(matching_indices) == 0:
        return 'N/A'
    
    # Perform statistical analysis
    mean = np.mean(matching_indices)
    variance = np.var(matching_indices)
    skewness = stats.skew(matching_indices)
    kurtosis = stats.kurtosis(matching_indices)
    
    # Plot the distribution of the indices
    plt.hist(matching_indices, bins='auto', color='blue', alpha=0.7)
    plt.title('Distribution of Matching Indices')
    plt.xlabel('Index')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the statistical results as a tuple
    return (mean, variance, skewness, kurtosis)