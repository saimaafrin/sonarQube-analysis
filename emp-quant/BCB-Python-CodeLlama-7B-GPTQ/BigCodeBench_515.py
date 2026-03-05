import pandas as pd
import seaborn as sns
def task_func(array):
    """
    Generates a DataFrame and heatmap from a 2D list.

    Parameters
    ----------
    array : 2D list
        The input array.

    Returns
    -------
    DataFrame
        Constructed from the input 2D list.
    heatmap
        Seaborn heatmap of the DataFrame's correlation matrix.

    Raises
    ------
    ValueError
        If the input array is empty or contains sublists of varying lengths.
    """
    # Check if the input array is empty or contains sublists of varying lengths
    if not array or len(array[0]) != 5:
        raise ValueError("Input array is empty or contains sublists of varying lengths.")

    # Construct a DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Compute the correlation matrix of the DataFrame
    corr = df.corr()

    # Generate a seaborn heatmap of the correlation matrix
    heatmap = sns.heatmap(corr, annot=True, cmap="coolwarm")

    return df, heatmap
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]