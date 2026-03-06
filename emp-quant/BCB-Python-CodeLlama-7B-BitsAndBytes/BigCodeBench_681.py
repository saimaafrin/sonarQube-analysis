
import pandas as pd
import json

def task_func(file_path, key):
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json(file_path, orient='records')

    # Remove the specified key from each object
    df = df.apply(lambda x: x.drop(key, axis=1))

    # Write the processed DataFrame back to a JSON file
    df.to_json(file_path, orient='records')

    return df