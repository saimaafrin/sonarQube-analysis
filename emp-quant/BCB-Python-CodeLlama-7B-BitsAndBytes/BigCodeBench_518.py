
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert 2D list to DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical labels to columns
    alphabet = [chr(i) for i in range(ord('A'), ord('A') + len(df.columns))]
    df.columns = alphabet

    # Compute Euclidean distance matrix
    distance_matrix = squareform(pdist(df, 'euclidean'))

    return df, distance_matrix