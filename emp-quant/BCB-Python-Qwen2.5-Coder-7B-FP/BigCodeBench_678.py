import pandas as pd
import json
import os
import shutil
def task_func(path):
    # Initialize an empty list to store DataFrames
    dfs = []
    
    # Ensure the processed directory exists
    processed_dir = os.path.join(path, 'processed')
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # List all JSON files in the directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]
    
    # Process each JSON file
    for json_file in sorted(json_files):
        # Construct the full file path
        file_path = os.path.join(path, json_file)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)
        
        # Insert the "Source" column
        df['Source'] = json_file
        
        # Append the DataFrame to the list
        dfs.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)
    
    # Move all processed JSON files to the "processed" subdirectory
    for json_file in json_files:
        shutil.move(os.path.join(path, json_file), processed_dir)
    
    return df