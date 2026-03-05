import pandas as pd
import os
def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)
    
    # Reverse the DataFrame
    df_reversed = df.iloc[::-1]
    
    # Write the reversed DataFrame back to the file, overwriting the original
    df_reversed.to_csv(filename, index=False)
    
    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as file:
        file.seek(0)
    
    # Return the filename
    return filename