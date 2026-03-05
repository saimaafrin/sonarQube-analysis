import pandas as pd
import seaborn as sns
import numpy as np
def task_func(array):
    """
    Generates a DataFrame and heatmap from a 2D list.
    This function takes a 2D list and returns a pandas DataFrame and a seaborn heatmap representing the correlation matrix of the DataFrame.
    Assumes sublists of length 5. Also assumes DataFrame columns: 'A', 'B', 'C', 'D', 'E'.
    The function should raise the exception for: ValueError: If the input array is empty or contains sublists of varying lengths.
    The function should output with:
        DataFrame: Constructed from the input 2D list.
        heatmap: Seaborn heatmap of the DataFrame's correlation matrix.
    """
    # Check if the input array is empty or contains sublists of varying lengths
    if len(array) == 0 or len(array[0]) != 5:
        raise ValueError("Input array is empty or contains sublists of varying lengths")

    # Construct a DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Compute the correlation matrix of the DataFrame
    corr = df.corr()

    # Generate a seaborn heatmap of the correlation matrix
    sns.heatmap(corr, annot=True, cmap='coolwarm')

    # Return the DataFrame and the heatmap
    return df, corr
array = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
    [4, 8, 12, 16, 20],
    [5, 10, 15, 20, 25]
]