
import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Creates a CSV file with random numeric data on the given file path.

    Parameters
    ----------
    file_path : str
        The file path to save the generated CSV file.
    num_rows : int
        The number of rows in the generated CSV file.
    data_dimensions : int, optional
        The number of columns (features) in the generated CSV file.
        Defaults to 5.
    random_seed : int, optional
        The random seed to use for generating random numbers.
        Defaults to None.

    Returns
    -------
    str
        The file path of the generated CSV file.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    data = np.random.rand(num_rows, data_dimensions)
    df = pd.DataFrame(data, columns=[f'Feature_{i}' for i in range(1, data_dimensions + 1)])
    df.to_csv(file_path, index=False)

    return file_path