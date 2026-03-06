import pandas as pd
from scipy.spatial.distance import pdist, squareform
def task_func(array):
    """
    Generate a Pandas DataFrame from a 2D list and calculate a distance matrix.

    This function converts a 2D list into a DataFrame, with columns named alphabetically starting from 'A'.
    It uses the `chr()` function, which converts an integer to its corresponding Unicode character,
    to dynamically assign alphabetical labels to each column based on their index. The function then
    computes the Euclidean distance matrix between rows.

    Parameters:
    array (list of list of int): The 2D list representing the data.
                                 Each sublist must contain only integers or floats. If the input does not
                                 conform to this structure, a TypeError is raised.

    Returns:
    - df (pd.DataFrame): data converted from 2D list.
    - distance_matrix (pd.DataFrame): output distance matrix.

    Requirements:
    - pandas
    - scipy.spatial.distance.pdist
    - scipy.spatial.distance.squareform

    Example:
    >>> df, distance_matrix = task_func([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D   E
    0  1  2  3  4   5
    1  6  7  8  9  10
    >>> print(distance_matrix)
              0         1
    0   0.00000  11.18034
    1  11.18034   0.00000
    """
    # Check if the input is a list of lists
    if not isinstance(array, list):
        raise TypeError("Input must be a list of lists.")
    if not all(isinstance(i, list) for i in array):
        raise TypeError("Input must be a list of lists.")
    if not all(isinstance(i, (int, float)) for i in array[0]):
        raise TypeError("Input must be a list of lists containing only integers or floats.")

    # Convert the 2D list into a DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical labels to each column
    for i in range(len(df.columns)):
        df.columns[i] = chr(65 + i)

    # Compute the Euclidean distance matrix
    distance_matrix = pd.DataFrame(squareform(pdist(df, 'euclidean')))

    return df, distance_matrix