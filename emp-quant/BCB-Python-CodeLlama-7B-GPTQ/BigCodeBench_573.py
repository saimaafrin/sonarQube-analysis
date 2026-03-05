import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.randint(1, 100, size=array_length)
    array2 = np.random.randint(1, 100, size=array_length)

    # Calculate mean, median, and standard deviation of each array
    mean1 = np.mean(array1)
    mean2 = np.mean(array2)
    median1 = np.median(array1)
    median2 = np.median(array2)
    std1 = np.std(array1)
    std2 = np.std(array2)

    # Store statistics in a Pandas DataFrame
    statistics = pd.DataFrame({
        'Array1': [mean1, median1, std1],
        'Array2': [mean2, median2, std2]
    }, index=['Mean', 'Median', 'Standard Deviation'])

    # Draw a bar chart to compare statistics
    fig, ax = plt.subplots()
    ax.bar(statistics.index, statistics['Array1'], label='Array1')
    ax.bar(statistics.index, statistics['Array2'], label='Array2')
    ax.set_title('Comparison of Statistics')
    ax.set_xlabel('Statistics')
    ax.set_ylabel('Values')
    ax.legend()
    plt.show()

    return statistics
array_length = 100