
import os
import random
import pandas as pd

def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):
    if seed is not None:
        random.seed(seed)
    selected_file = random.choice(csv_files)
    selected_file_path = os.path.join(data_dir, selected_file)
    selected_rows = pd.read_csv(selected_file_path, nrows=10)
    return (selected_file, selected_rows)