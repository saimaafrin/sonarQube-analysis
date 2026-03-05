
import os
import pandas as pd

def task_func(filename: str) -> pd.DataFrame:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    df = pd.read_csv(filename)
    
    # Delete the original file
    os.remove(filename)
    
    return df