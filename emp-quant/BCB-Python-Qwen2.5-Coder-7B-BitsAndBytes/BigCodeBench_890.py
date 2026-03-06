
import os
import random
import pandas as pd

def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Randomly select a CSV file
    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {selected_file} does not exist in the directory {data_dir}.")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the DataFrame is empty
    if df.empty:
        return selected_file, pd.DataFrame()
    
    # Select a random sample of 5 records (or fewer if the file has less than 5 records)
    num_records = min(5, len(df))
    sampled_df = df.sample(n=num_records, random_state=seed)
    
    return selected_file, sampled_df