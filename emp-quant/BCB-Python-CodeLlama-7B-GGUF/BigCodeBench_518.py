
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert 2D list to DataFrame
    df = pd.DataFrame(array)

    # Assign alphabetical column labels
    df.columns = [chr(i) for i in range(65, 65 + len(df.columns))]

    # Compute Euclidean distance matrix
    distance_matrix = squareform(pdist(df, 'euclidean'))

    return df, distance_matrix