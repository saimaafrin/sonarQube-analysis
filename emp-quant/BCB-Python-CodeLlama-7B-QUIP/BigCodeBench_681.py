
import pandas as pd
import json

def task_func(file_path, key):
    # Load the JSON file into a DataFrame
    df = pd.read_json(file_path)

    # Remove the specified key from each object
    df = df.drop(key, axis=1)

    # Write the processed DataFrame back to a JSON file
    with open(file_path, 'w') as f:
        json.dump(df, f, indent=4)

    return df