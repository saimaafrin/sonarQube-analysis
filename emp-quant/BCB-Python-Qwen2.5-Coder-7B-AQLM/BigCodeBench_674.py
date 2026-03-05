
import pandas as pd
import os

def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    # Read the CSV file
    df = pd.read_csv(filename)

    # Reverse the order of the lines, excluding the header
    df_reversed = df.iloc[::-1]

    # Write the reversed lines back to the file
    with open(filename, 'w', newline='') as file:
        df_reversed.to_csv(file, index=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r') as file:
        file.seek(0)

    # Return the filename
    return filename