
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    """
    Convert a 2D list into a Pandas DataFrame and calculate the Euclidean distance matrix.

    Parameters:
    array (list of lists): The 2D list to be converted into a DataFrame.

    Returns:
    df (pd.DataFrame): The DataFrame created from the 2D list.
    distance_matrix (pd.DataFrame): The Euclidean distance matrix between rows of the DataFrame.
    """
    # Convert the 2D list into a DataFrame
    df = pd.DataFrame(array, columns=[chr(65 + i) for i in range(len(array[0]))])
    
    # Calculate the Euclidean distance matrix
    distance_matrix = squareform(pdist(df, 'euclidean'))
    
    # Convert the distance matrix to a DataFrame
    distance_matrix = pd.DataFrame(distance_matrix, index=df.index, columns=df.index)
    
    return df, distance_matrix