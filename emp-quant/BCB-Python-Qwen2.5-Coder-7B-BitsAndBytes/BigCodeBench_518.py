
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    """
    Convert a 2D list into a Pandas DataFrame and compute the Euclidean distance matrix.

    Parameters:
    array (list of lists): A 2D list where each sublist represents a row in the DataFrame.

    Returns:
    df (pd.DataFrame): Dataframe created from the input 2D list.
    distance_matrix (pd.DataFrame): Distance matrix computed using Euclidean distance.
    """
    # Create DataFrame from the 2D list
    df = pd.DataFrame(array)
    
    # Dynamically generate column names starting from 'A'
    columns = [chr(65 + i) for i in range(df.shape[1])]
    df.columns = columns
    
    # Compute the Euclidean distance matrix
    distance_matrix = pd.DataFrame(squareform(pdist(df, metric='euclidean')), 
                                  columns=columns, index=columns)
    
    return df, distance_matrix