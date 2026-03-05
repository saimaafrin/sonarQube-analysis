import os
import pandas as pd
def task_func(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist")

    df = pd.read_csv(filename)
    with open(filename, "w") as f:
        f.truncate()

    return df