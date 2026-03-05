import pandas as pd
from scipy.spatial.distance import pdist, squareform
def task_func(array):
    """
    Generate a Pandas DataFrame from a 2D list and calculate a distance matrix.

    Parameters
    ----------
    array : 2D list
        Input data.

    Returns
    -------
    df (pd.DataFrame): data converted from 2D list.
    distance_matrix (pd.DataFrame): output distance matrix.
    """
    # Convert 2D list to Pandas DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical labels to columns
    df.columns = [chr(i) for i in range(65, 65 + df.shape[1])]

    # Compute Euclidean distance matrix
    distance_matrix = squareform(pdist(df, 'euclidean'))

    return df, distance_matrix
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]