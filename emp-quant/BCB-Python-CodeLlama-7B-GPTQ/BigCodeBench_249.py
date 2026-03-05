import pandas as pd
import random
from sklearn.model_selection import train_test_split
def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    """
    Generate a random set of floating-point numbers within a specified range, truncate each value to 3 decimal places, and divide the data into train and test sets based on a given test size.

    Args:
        n_data_points (int): Number of data points to generate.
        min_value (float): Minimum value of the generated data.
        max_value (float): Maximum value of the generated data.
        test_size (float): Test size (fraction of data to be used for testing).

    Returns:
        tuple: A tuple with two pandas DataFrames (train set, test set).
    """
    # Generate random data
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]

    # Truncate data to 3 decimal places
    data = [round(x, 3) for x in data]

    # Divide data into train and test sets
    train_data, test_data = train_test_split(data, test_size=test_size)

    # Create pandas DataFrames
    train_df = pd.DataFrame({'Value': train_data})
    test_df = pd.DataFrame({'Value': test_data})

    return train_df, test_df