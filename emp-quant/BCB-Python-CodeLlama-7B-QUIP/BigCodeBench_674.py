
import pandas as pd
import os

def task_func(filename):
    # Read the CSV file
    df = pd.read_csv(filename)

    # Reverse the order of the lines
    df = df.iloc[::-1]

    # Write the inverted lines back to the file
    df.to_csv(filename, index=False, header=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as f:
        f.seek(0)

    return filename