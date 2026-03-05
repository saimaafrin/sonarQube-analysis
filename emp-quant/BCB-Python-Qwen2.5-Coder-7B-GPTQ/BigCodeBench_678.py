import pandas as pd
import json
import os
import shutil
def task_func(path):
    # Ensure the processed directory exists
    processed_dir = os.path.join(path, 'processed')
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # Initialize an empty list to store DataFrames
    dfs = []

    # List all JSON files in the directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]

    # Process each JSON file
    for json_file in sorted(json_files):
        file_path = os.path.join(path, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            df['Source'] = json_file
            dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)

    # Move all JSON files to the processed directory
    for json_file in json_files:
        shutil.move(os.path.join(path, json_file), os.path.join(processed_dir, json_file))

    return df