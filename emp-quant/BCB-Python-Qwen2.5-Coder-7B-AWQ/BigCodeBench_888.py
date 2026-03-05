import pandas as pd
import os
def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    # Check if the list of CSV files is empty
    if not csv_files:
        return pd.DataFrame()
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Loop through each CSV file in the list
    for file in csv_files:
        # Construct the full file path
        file_path = os.path.join(data_dir, file)
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the CSV file into a DataFrame and append to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)
    
    # Concatenate all DataFrames in the list into a single DataFrame
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    return merged_df