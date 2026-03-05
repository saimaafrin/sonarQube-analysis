import os
import random
import pandas as pd
def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):
    """
    Randomly select one of the provided csv_files and select a certain number of records from the file at random. The selected records are returned in a DataFrame. The name of the selected csv_file is also returned. If the csv_file is empty return an empty DataFrame.
    """
    if seed is not None:
        random.seed(seed)

    # Select a random file from the list of files
    selected_file = random.choice(csv_files)

    # Read the selected file into a DataFrame
    df = pd.read_csv(os.path.join(data_dir, selected_file))

    # Select a random number of rows from the DataFrame
    num_rows = random.randint(1, len(df))
    selected_rows = df.sample(n=num_rows)

    # Return the selected rows and the name of the selected file
    return (selected_file, selected_rows)
data_dir = 'data'
csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
seed = random.randint(1, 100)