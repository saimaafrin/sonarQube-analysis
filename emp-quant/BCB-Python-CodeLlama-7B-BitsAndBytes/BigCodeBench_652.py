
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])

def task_func(target_value=TARGET_VALUE, array=ARRAY):
    # Find the row indices where the first cell matches target_value
    indices = np.where(array[0] == target_value)[0]

    # Perform statistical analysis on the indices
    if len(indices) == 0:
        return 'N/A'
    else:
        mean = np.mean(indices)
        variance = np.var(indices)
        skewness = stats.skew(indices)
        kurtosis = stats.kurtosis(indices)
        return (mean, variance, skewness, kurtosis)

# Plot the distribution of the indices
plt.hist(indices, bins=20)
plt.xlabel('Indices')
plt.ylabel('Frequency')
plt.title('Distribution of Indices')
plt.show()

# Print the results
print(task_func())