import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)

    # Calculate mean, median, and standard deviation of arrays
    mean1 = np.mean(array1)
    mean2 = np.mean(array2)
    median1 = np.median(array1)
    median2 = np.median(array2)
    std1 = np.std(array1)
    std2 = np.std(array2)

    # Create a Pandas DataFrame with the statistics
    statistics = pd.DataFrame({'Array1': [mean1, median1, std1],
                               'Array2': [mean2, median2, std2]},
                               index=['Mean', 'Median', 'Standard Deviation'])

    # Draw a bar chart to compare the statistics
    plt.bar(statistics.index, statistics.values)
    plt.xlabel('Statistic')
    plt.ylabel('Value')
    plt.title('Comparison of Statistics')
    plt.show()

    return statistics
array_length = 100