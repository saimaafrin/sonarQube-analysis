import os
import random
import pandas as pd
import unittest
def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):
    """
    Randomly select one of the provided csv_files and select a certain number of records from the file at random. The selected records are returned in a DataFrame. The name of the selected csv_file is also returned. If the csv_file is empty return an empty DataFrame.
    """
    if seed is not None:
        random.seed(seed)
    csv_file = random.choice(csv_files)
    csv_path = os.path.join(data_dir, csv_file)
    if not os.path.exists(csv_path):
        return pd.DataFrame()
    df = pd.read_csv(csv_path)
    num_rows = random.randint(1, len(df))
    selected_rows = df.sample(n=num_rows)
    return (csv_file, selected_rows)