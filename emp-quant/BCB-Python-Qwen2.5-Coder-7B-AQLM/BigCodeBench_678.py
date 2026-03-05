
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Initialize an empty list to store DataFrames
    dfs = []
    
    # Create the "processed" directory if it doesn't exist
    processed_dir = os.path.join(path, 'processed')
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Get a list of all JSON files in the directory and sort them alphabetically
    json_files = sorted([f for f in os.listdir(path) if f.endswith('.json')])
    
    # Process each JSON file
    for json_file in json_files:
        # Construct the full file path
        file_path = os.path.join(path, json_file)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Convert the JSON data to a DataFrame
        df = pd.DataFrame(data)
        
        # Add a "Source" column with the filename
        df['Source'] = json_file
        
        # Append the DataFrame to the list
        dfs.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)
    
    # Move all processed JSON files to the "processed" directory
    for json_file in json_files:
        shutil.move(os.path.join(path, json_file), os.path.join(processed_dir, json_file))
    
    return df