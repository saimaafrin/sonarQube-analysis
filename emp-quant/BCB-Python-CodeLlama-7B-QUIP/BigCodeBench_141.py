
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if rows <= 0:
        raise ValueError("'rows' must be a positive integer greater than 0")

    # Generate random numbers for each column
    data = np.random.default_rvs(size=(rows, len(columns)), seed=seed)

    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=columns)

    # Calculate the mean and median for each column
    means = {column: statistics.mean(df[column]) for column in columns}
    medians = {column: statistics.median(df[column]) for column in columns}

    return df, means, medians