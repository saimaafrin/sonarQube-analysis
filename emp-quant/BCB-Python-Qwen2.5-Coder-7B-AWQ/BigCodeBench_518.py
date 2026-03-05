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
    df = pd.DataFrame(array)
    
    # Dynamically assign alphabetical labels to each column
    df.columns = [chr(65 + i) for i in range(df.shape[1])]
    
    # Calculate the Euclidean distance matrix
    distance_matrix = pd.DataFrame(squareform(pdist(df, 'euclidean')), 
                                  columns=df.columns, 
                                  index=df.columns)
    
    return df, distance_matrix
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]