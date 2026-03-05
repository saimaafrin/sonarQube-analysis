import os
import pandas as pd
def task_func(filename: str) -> pd.DataFrame:
    # Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)
    
    # Delete the entire contents of the original file
    with open(filename, 'w') as file:
        file.truncate(0)
    
    return df