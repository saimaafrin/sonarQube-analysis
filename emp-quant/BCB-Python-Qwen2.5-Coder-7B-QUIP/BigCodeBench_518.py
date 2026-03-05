
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert the 2D list to a DataFrame
    df = pd.DataFrame(array, columns=[chr(65 + i) for i in range(len(array[0]))])
    
    # Calculate the Euclidean distance matrix
    distance_matrix = pd.DataFrame(pdist(df, metric='euclidean'), columns=df.columns, index=df.columns)
    
    return df, distance_matrix