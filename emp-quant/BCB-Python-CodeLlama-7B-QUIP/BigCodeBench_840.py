
import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Creates a CSV file with random numeric data.

    Parameters:
    file_path (str): The file path to save the generated CSV file.
    num_rows (int): The number of rows in the generated CSV file.
    data_dimensions (int): The number of columns (features) in the generated CSV file.
    random_seed (int): The random seed to use for generating random numbers.

    Returns:
    str: The file path of the generated CSV file.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate random data
    data = np.random.rand(num_rows, data_dimensions)

    # Create the CSV file
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    return file_path