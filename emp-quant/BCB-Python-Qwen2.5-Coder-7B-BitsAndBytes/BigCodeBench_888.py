
import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    if not csv_files:
        return pd.DataFrame()
    
    # Initialize an empty list to store DataFrames
    df_list = []
    
    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        if os.path.exists(file_path):
            # Read each CSV file and append to the list
            df_list.append(pd.read_csv(file_path))
    
    # Concatenate all DataFrames in the list
    result_df = pd.concat(df_list, ignore_index=True)
    
    return result_df