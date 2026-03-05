
import pandas as pd
from scipy import stats

def task_func(matrix):
    # Convert the input matrix to a DataFrame
    df = pd.DataFrame(matrix)
    
    # Normalize the DataFrame using the Z-score
    normalized_df = stats.zscore(df, axis=0)
    
    # Return the normalized DataFrame
    return normalized_df