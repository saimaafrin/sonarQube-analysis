
import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    # Check if the list of CSV files is empty
    if not csv_files:
        return pd.DataFrame()

    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()

    # Loop through the list of CSV files
    for file in csv_files:
        # Construct the full file path
        file_path = os.path.join(data_dir, file)
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Append the DataFrame to the merged DataFrame
            merged_df = pd.concat([merged_df, df], ignore_index=True)

    # Return the merged DataFrame
    return merged_df