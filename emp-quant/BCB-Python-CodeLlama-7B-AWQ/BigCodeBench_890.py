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

    # Select a random csv file
    selected_file = random.choice(csv_files)

    # Check if the selected file is empty
    if os.stat(os.path.join(data_dir, selected_file)).st_size == 0:
        return (selected_file, pd.DataFrame())

    # Read the selected file
    df = pd.read_csv(os.path.join(data_dir, selected_file))

    # Select a random number of records from the file
    num_records = random.randint(1, len(df))
    selected_rows = random.sample(df.index, num_records)

    # Return the selected file and the selected records
    return (selected_file, df.iloc[selected_rows])
data_dir = 'data'
csv_files = ['file1.csv', 'file2.csv', 'file3.csv']