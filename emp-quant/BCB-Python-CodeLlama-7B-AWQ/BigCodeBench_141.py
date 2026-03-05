import numpy as np
import pandas as pd
import statistics
def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    """
    Create a Pandas DataFrame with a specified number of rows and six columns (default A-F), each filled with random numbers between 1 and 100, using a specified seed for reproducibility. Additionally, calculate the mean and median for each column.
    The function should raise the exception for: ValueError: If 'rows' is not a positive integer greater than 0.
    The function should output with:
        DataFrame: A pandas DataFrame with the generated data.
        dict: A dictionary containing the calculated mean and median for each column.
        The dictionary format is:
        {
        'ColumnName': {
        'mean': MeanValue,
        'median': MedianValue
        }, ...
        }
        where 'ColumnName' is each of the specified column names, 'MeanValue' is the calculated mean,
        and 'MedianValue' is the calculated median for that column.
    """
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("'rows' must be a positive integer greater than 0")

    # Generate random data
    np.random.seed(seed)
    data = np.random.randint(1, 100, size=(rows, len(columns)))

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Calculate mean and median for each column
    means = {}
    medians = {}
    for col in columns:
        means[col] = df[col].mean()
        medians[col] = df[col].median()

    return df, means, medians