
import os
import pandas as pd

def task_func(filename: str) -> pd.DataFrame:
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        
        # Delete the entire contents of the original file
        open(filename, 'w').close()
        
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} does not exist.")