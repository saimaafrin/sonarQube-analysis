
import os
import pandas as pd

def task_func(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The contents of the CSV file as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist.")

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)

    # Delete the contents of the original file
    with open(filename, "w") as f:
        f.truncate(0)

    return df