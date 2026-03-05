import pandas as pd
import time
import os
OUTPUT_DIR = './output'
def task_func(df: pd.DataFrame, filename: str) -> str:
    """
    Write a Pandas DataFrame into a JSON Lines file and save it in a specified directory.

    Args:
        df (pd.DataFrame): The Pandas DataFrame to be written to the JSON Lines file.
        filename (str): The name of the JSON Lines file to be saved.

    Returns:
        str: The full path where the JSON Lines file was saved.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Write the DataFrame to a JSON Lines file
    df.to_json(os.path.join(OUTPUT_DIR, filename), orient='records', lines=True)

    # Return the full path of the JSON Lines file
    return os.path.join(OUTPUT_DIR, filename)
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [24, 30, 36]})
filename = 'data.jsonl'