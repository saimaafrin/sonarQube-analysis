
import pandas as pd
import os

def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Reverse the order of the rows
    reversed_df = df.iloc[::-1]
    
    # Write the reversed DataFrame back to the file
    reversed_df.to_csv(filename, index=False)
    
    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as f:
        f.seek(0)
    
    return filename