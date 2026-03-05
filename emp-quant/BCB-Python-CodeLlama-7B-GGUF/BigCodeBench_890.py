
import os
import random
import pandas as pd

def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Get the list of files in the data directory
    files = os.listdir(data_dir)

    # Filter the list of files to only include the csv files
    csv_files = [f for f in files if f.endswith('.csv')]

    # Check if there are any csv files in the directory
    if not csv_files:
        return pd.DataFrame(), 'No csv files found in the directory'

    # Select a random file from the list of csv files
    random_file = random.choice(csv_files)

    # Read the selected file into a pandas DataFrame
    df = pd.read_csv(os.path.join(data_dir, random_file))

    # Select a random number of rows from the DataFrame
    num_rows = random.randint(1, len(df))
    selected_rows = df.sample(n=num_rows)

    # Return the selected rows and the name of the selected file
    return selected_rows, random_file