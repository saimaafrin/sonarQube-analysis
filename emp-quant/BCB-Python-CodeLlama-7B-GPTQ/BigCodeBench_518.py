import pandas as pd
from scipy.spatial.distance import pdist, squareform
def task_func(array):
    """
    Generate a Pandas DataFrame from a 2D list and calculate a distance matrix.
    This function converts a 2D list into a DataFrame, with columns named alphabetically starting from 'A'. It uses the `chr()` function, which converts an integer to its corresponding Unicode character, to dynamically assign alphabetical labels to each column based on their index. The function then computes the Euclidean distance matrix between rows.
    """
    # Convert 2D list to Pandas DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical labels to columns
    columns = [chr(ord('A') + i) for i in range(df.shape[1])]
    df.columns = columns

    # Compute Euclidean distance matrix
    distance_matrix = squareform(pdist(df, 'euclidean'))

    return df, distance_matrix
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]