import pandas as pd
import json
def task_func(file_path, key):
    """
    Load a JSON file into a Pandas DataFrame, remove a specific key from each object, and write the processed DataFrame back into a JSON file oriented by records.
    :param file_path: Path to the JSON file to be processed.
    :param key: Key to be removed from each object in the JSON file.
    :return: A Pandas DataFrame representation of the processed JSON data.
    """
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json(file_path, orient='records')

    # Remove the specified key from each object in the DataFrame
    df = df.apply(lambda x: x.pop(key, None))

    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json(file_path, orient='records', indent=4)

    return df
file_path = 'data.json'
key = 'id'