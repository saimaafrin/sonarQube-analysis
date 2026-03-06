
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Ensure the processed directory exists
    processed_path = os.path.join(path, 'processed')
    if not os.path.exists(processed_path):
        os.makedirs(processed_path)

    # Initialize an empty list to store DataFrames
    dfs = []

    # List all JSON files in the directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]

    # Process each JSON file
    for json_file in sorted(json_files):
        file_path = os.path.join(path, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data)
        
        # Insert 'Source' column
        df['Source'] = json_file
        
        # Append DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames into one
    df = pd.concat(dfs, ignore_index=True)

    # Move all processed JSON files to the 'processed' directory
    for json_file in json_files:
        src_path = os.path.join(path, json_file)
        dst_path = os.path.join(processed_path, json_file)
        shutil.move(src_path, dst_path)

    return df