import numpy as np
import pandas as pd
def task_func(array_length=100):
    '''
    Generate two arrays of random numbers of a given length, calculate their mean, median, and standard deviation,
    then store these results in a Panda DataFrame 'statistics' with keys 'Array1' and 'Array2'.
    Draw a bar chart to compare these statistics with indices 'Mean', 'Median', and 'Standard Deviation'.

    Parameters:
    - array_length (int, optional): The length of the arrays to be generated. Default is 100.

    Returns:
    - DataFrame: A pandas DataFrame with the statistics of the arrays.
    - Axes: The bar chart plot comparing the statistics.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> df, ax = task_func(50)
    '''
    array1 = np.random.randint(0, 100, array_length)
    array2 = np.random.randint(0, 100, array_length)
    statistics = pd.DataFrame({'Array1': array1, 'Array2': array2})
    statistics['Mean'] = statistics.mean(axis=1)
    statistics['Median'] = statistics.median(axis=1)
    statistics['Standard Deviation'] = statistics.std(axis=1)
    ax = statistics.plot(kind='bar', figsize=(10, 5), rot=0, legend=False)
    ax.set_xlabel('Array')
    ax.set_ylabel('Statistic')
    ax.set_title('Comparison of Statistics')
    ax.set_xticklabels(['Array1', 'Array2'])
    ax.set_ylim(0, 100)
    return statistics, ax