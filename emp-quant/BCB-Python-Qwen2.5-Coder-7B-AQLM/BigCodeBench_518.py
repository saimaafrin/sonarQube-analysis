
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def task_func(array):
    # Convert 2D list to DataFrame
    df = pd.DataFrame(array)
    # Dynamically assign alphabetical column labels
    df.columns = [chr(65 + i) for i in range(df.shape[1])]
    
    # Calculate the Euclidean distance matrix
    distance_matrix = pd.DataFrame(squareform(pdist(df, 'euclidean')), 
                                  columns=df.columns, 
                                  index=df.columns)
    
    return df, distance_matrix