
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Create the processed directory if it doesn't exist
    if not os.path.exists(os.path.join(path, 'processed')):
        os.makedirs(os.path.join(path, 'processed'))

    # Read all JSON files in the directory and create a DataFrame
    files = [f for f in os.listdir(path) if f.endswith('.json')]
    dfs = [pd.read_json(os.path.join(path, f)) for f in files]
    df = pd.concat(dfs, ignore_index=True)

    # Add a "Source" column to the DataFrame
    df['Source'] = [f.split('.')[0] for f in files]

    # Move the processed files to the "processed" subdirectory
    for f in files:
        shutil.move(os.path.join(path, f), os.path.join(path, 'processed', f))

    return df