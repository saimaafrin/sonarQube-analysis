import pandas as pd
import numpy as np
def task_func(data, cols):
    """
    Turn the provided data into a DataFrame and then calculate the correlation matrix of numeric columns.
    """
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=np.number)

    # Calculate the correlation matrix
    correlation_matrix = numeric_cols.corr()

    return correlation_matrix
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
cols = ['a', 'b', 'c']