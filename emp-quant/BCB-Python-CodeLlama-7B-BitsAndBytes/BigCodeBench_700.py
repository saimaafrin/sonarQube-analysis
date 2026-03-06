
import pandas as pd
import numpy as np

def task_func(data, cols):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=cols)

    # Calculate the correlation matrix of the numeric columns
    correlation_matrix = df.corr()

    # Output the correlation matrix
    print(correlation_matrix)