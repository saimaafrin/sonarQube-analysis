
import os
import random
import pandas as pd

def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    if seed is not None:
        random.seed(seed)
    
    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_dir, selected_file)
    
    if not os.path.exists(file_path):
        return selected_file, pd.DataFrame()
    
    df = pd.read_csv(file_path)
    
    if df.empty:
        return selected_file, pd.DataFrame()
    
    num_records = random.randint(1, len(df))
    selected_df = df.sample(n=num_records, random_state=seed)
    
    return selected_file, selected_df