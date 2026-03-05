
import pandas as pd
import os

def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Reverse the order of the lines, excluding the header
    reversed_df = df.iloc[::-1]
    
    # Write the reversed lines back to the file, excluding the header
    reversed_df.to_csv(filename, index=False, header=False)
    
    # Move the cursor back to the beginning of the file
    with open(filename, 'a') as file:
        file.seek(0)
    
    return filename