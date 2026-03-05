
import os
import pandas as pd

def task_func(filename: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filename)
        os.remove(filename)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} does not exist")