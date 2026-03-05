import numpy as np
import pandas as pd
import statistics
def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    """
    Creates a Pandas DataFrame with a specified number of rows and six columns (default A-F), each filled with random numbers between 1 and 100, using a specified seed for reproducibility. Additionally, calculates the mean and median for each column.
    """
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("'rows' must be a positive integer greater than 0.")

    # Generate random numbers between 1 and 100 for each column
    data = np.random.randint(1, 100, size=(rows, len(columns)))

    # Create a Pandas DataFrame with the generated data
    df = pd.DataFrame(data, columns=columns)

    # Calculate the mean and median for each column
    means = df.mean(axis=0)
    medians = df.median(axis=0)

    # Create a dictionary with the calculated mean and median for each column
    result = {column: {'mean': mean, 'median': median} for column, mean, median in zip(columns, means, medians)}

    return df, result
rows = 10
columns = ['A', 'B', 'C', 'D', 'E', 'F']
seed = 42