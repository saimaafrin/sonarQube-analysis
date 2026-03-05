
import pandas as pd
import os

def task_func(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename, header=0, index_col=None)

    # Reverse the order of the DataFrame
    df_reversed = df.iloc[::-1]

    # Write the reversed DataFrame back to the file
    df_reversed.to_csv(filename, index=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as f:
        f.seek(0)

    return filename