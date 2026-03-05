import pandas as pd
import numpy as np
def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Generates a CSV file with random numeric data.

    Parameters:
    - file_path (str): The path where the CSV file will be saved.
    - num_rows (int): The number of rows in the CSV file.
    - data_dimensions (int): The number of columns (features) in the CSV file.
    - random_seed (int, optional): Seed for the random number generator for reproducibility.

    Returns:
    - str: The file path of the generated CSV file.
    """
    # Set the random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate random data
    data = np.random.rand(num_rows, data_dimensions)

    # Create DataFrame with column names 'Feature_1', 'Feature_2', ..., 'Feature_n'
    column_names = [f'Feature_{i+1}' for i in range(data_dimensions)]
    df = pd.DataFrame(data, columns=column_names)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    return file_path