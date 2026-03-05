
import os
import random
import pandas as pd

def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Randomly select one of the csv_files
    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file is empty
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return selected_file, pd.DataFrame()
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the DataFrame is empty
    if df.empty:
        return selected_file, pd.DataFrame()
    
    # Select a random number of records from the DataFrame
    num_records = random.randint(1, len(df))
    selected_df = df.sample(n=num_records, random_state=seed)
    
    return selected_file, selected_df