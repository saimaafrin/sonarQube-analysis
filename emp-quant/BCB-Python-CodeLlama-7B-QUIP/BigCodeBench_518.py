
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert 2D list to DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical labels to columns
    for i in range(df.shape[1]):
        df.columns[i] = chr(i + 1)

    # Compute Euclidean distance matrix
    distance_matrix = pdist(df, 'euclidean')

    # Output distance matrix
    return distance_matrix