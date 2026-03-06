import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists
    with indices 'A' and 'B', and then draw the values with a line displaying the Euclidean distance.

    Parameters:
    a (list): A list of numbers.
    b (list): Another list of numbers.

    Returns:
    float: The computed Euclidean distance between the two lists.
    pd.DataFrame: A DataFrame containing the two lists as columns.
    matplotlib.axes.Axes: The generated plot's Axes object.

    Requirements:
    - pandas
    - scipy.spatial
    - matplotlib.pyplot

    Example:
    >>> euclidean_distance, df, ax = task_func([1, 2, 3], [2, 3, 4])
    >>> print(euclidean_distance)
    1.7320508075688772
    """
    euclidean_distance = distance.euclidean(a, b)
    df = pd.DataFrame({'A': a, 'B': b})
    ax = df.plot.line(x='A', y='B')
    ax.set_title('Euclidean distance between two lists')
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_xticks(df['A'])
    ax.set_yticks(df['B'])
    ax.set_xticklabels(df['A'])
    ax.set_yticklabels(df['B'])
    ax.axvline(euclidean_distance, color='red')
    ax.axhline(euclidean_distance, color='red')
    return euclidean_distance, df, ax