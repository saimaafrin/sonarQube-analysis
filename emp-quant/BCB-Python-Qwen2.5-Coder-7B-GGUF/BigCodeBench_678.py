
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Ensure the processed directory exists
    processed_path = os.path.join(path, 'processed')
    if not os.path.exists(processed_path):
        os.makedirs(processed_path)

    # Initialize an empty DataFrame to store the data
    df = pd.DataFrame()

    # List all JSON files in the directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]

    # Process each JSON file
    for file in sorted(json_files):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Convert the data to a DataFrame and add a 'Source' column
        temp_df = pd.DataFrame(data)
        temp_df['Source'] = file
        
        # Append the DataFrame to the main DataFrame
        df = pd.concat([df, temp_df], ignore_index=True)
        
        # Move the processed file to the 'processed' subdirectory
        shutil.move(file_path, os.path.join(processed_path, file))

    return df