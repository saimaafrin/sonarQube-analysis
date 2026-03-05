import pandas as pd
import os
def task_func(filename):
    """
    Read a CSV file of pandas, reverse the order of the lines and write the inverted lines back into the file. Then move the cursor back to the beginning of the file. The header should not be inverted and the file may be empty.
    """
    # Read the CSV file
    df = pd.read_csv(filename)

    # Reverse the order of the lines
    df = df.iloc[::-1]

    # Write the inverted lines back into the file
    df.to_csv(filename, index=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as f:
        f.seek(0)

    return filename
filename = 'test.csv'