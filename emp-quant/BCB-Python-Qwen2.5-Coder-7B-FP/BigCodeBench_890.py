import os
import random
import pandas as pd
def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Randomly select a csv file
    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {selected_file} does not exist in the directory {data_dir}.")
    
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return selected_file, pd.DataFrame()
    
    # If the DataFrame is empty, return an empty DataFrame
    if df.empty:
        return selected_file, pd.DataFrame()
    
    # Randomly select a certain number of records from the DataFrame
    num_records = random.randint(1, len(df))
    selected_df = df.sample(n=num_records, random_state=seed)
    
    return selected_file, selected_df