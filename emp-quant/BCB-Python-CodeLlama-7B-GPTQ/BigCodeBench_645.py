import os
import pandas as pd
def task_func(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.
    The function should raise the exception for: FileNotFoundError: If the CSV file does not exist.
    The function should output with:
        DataFrame: The contents of the CSV file as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filename)
        with open(filename, 'w') as f:
            f.truncate()
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f'File {filename} does not exist') from e