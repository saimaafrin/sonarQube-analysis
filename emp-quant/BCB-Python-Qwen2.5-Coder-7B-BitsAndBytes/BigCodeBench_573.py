
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)

    # Calculate mean, median, and standard deviation for each array
    stats_array1 = {
        'Mean': np.mean(array1),
        'Median': np.median(array1),
        'Standard Deviation': np.std(array1)
    }
    stats_array2 = {
        'Mean': np.mean(array2),
        'Median': np.median(array2),
        'Standard Deviation': np.std(array2)
    }

    # Store results in a Pandas DataFrame
    statistics = pd.DataFrame({
        'Array1': [stats_array1['Mean'], stats_array1['Median'], stats_array1['Standard Deviation']],
        'Array2': [stats_array2['Mean'], stats_array2['Median'], stats_array2['Standard Deviation']]
    }, index=['Mean', 'Median', 'Standard Deviation'])

    # Draw a bar chart to compare these statistics
    statistics.plot(kind='bar')
    plt.title('Comparison of Statistics for Two Arrays')
    plt.ylabel('Values')
    plt.show()

    return statistics