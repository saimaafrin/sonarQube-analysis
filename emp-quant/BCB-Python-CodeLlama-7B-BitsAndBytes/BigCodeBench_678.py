
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Create the processed directory if it doesn't exist
    if not os.path.exists('processed'):
        os.makedirs('processed')

    # Read all JSON files in the directory and sort them alphabetically
    files = [f for f in os.listdir(path) if f.endswith('.json')]
    files.sort()

    # Create a list to store the data from each file
    data = []

    # Process each file and add the source column
    for file in files:
        with open(os.path.join(path, file), 'r') as f:
            data.append(pd.read_json(f, orient='records'))
            data[-1]['Source'] = file

    # Concatenate the data from all files into a single DataFrame
    df = pd.concat(data, ignore_index=True)

    # Move the processed files to the processed directory
    for file in files:
        shutil.move(os.path.join(path, file), 'processed')

    return df

# Call the function with the path to the directory containing the JSON files
df = task_func('path/to/directory')

# Print the DataFrame
print(df)