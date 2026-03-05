import pandas as pd
import json
import os
import shutil
def task_func(path):
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Ensure the path exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Ensure the processed directory exists
    processed_path = os.path.join(path, 'processed')
    if not os.path.exists(processed_path):
        os.makedirs(processed_path)
    
    # List all JSON files in the directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]
    
    # Sort the JSON files alphabetically
    json_files.sort()
    
    # Process each JSON file
    for json_file in json_files:
        # Construct the full file path
        file_path = os.path.join(path, json_file)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)
        
        # Insert a "Source" column
        df['Source'] = json_file
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    df = pd.concat(dataframes, ignore_index=True)
    
    # Move all JSON files to the processed directory
    for json_file in json_files:
        shutil.move(os.path.join(path, json_file), os.path.join(processed_path, json_file))
    
    return df