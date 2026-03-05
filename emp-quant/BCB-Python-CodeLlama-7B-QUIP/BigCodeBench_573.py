
import numpy as np
import pandas as pd

def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)

    # Calculate the mean, median, and standard deviation of the arrays
    mean1 = np.mean(array1)
    median1 = np.median(array1)
    std1 = np.std(array1)
    mean2 = np.mean(array2)
    median2 = np.median(array2)
    std2 = np.std(array2)

    # Create a DataFrame with the statistics
    statistics = pd.DataFrame({
        'Array1': [mean1, median1, std1],
        'Array2': [mean2, median2, std2]
    }, index=['Mean', 'Median', 'Standard Deviation'])

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar('Array1', statistics['Array1'])
    ax.bar('Array2', statistics['Array2'])
    ax.set_ylabel('Value')
    ax.set_xlabel('Array')
    ax.set_title('Statistics')
    plt.show()

    return statistics