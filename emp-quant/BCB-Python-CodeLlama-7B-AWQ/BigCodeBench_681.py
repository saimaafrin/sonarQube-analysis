import pandas as pd
import json
def task_func(file_path, key):
    """
    Load a JSON file into a Pandas DataFrame, remove a specific key from each object, and write the processed DataFrame back into a JSON file oriented by records.
    """
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json(file_path, orient='records')

    # Remove the specified key from each object
    df = df.apply(lambda x: x.drop(key, axis=1))

    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json(file_path, orient='records')

    return df
file_path = 'data.json'
key = 'id'