import pandas as pd
import time
import os
OUTPUT_DIR = './output'
def task_func(df: pd.DataFrame, filename: str) -> str:
    """
    Write a Pandas DataFrame into a JSON Lines file and save it in a specified directory.
    The function should output with:
        str: The full path where the JSON Lines file was saved.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Save the DataFrame to a JSON Lines file
    filepath = os.path.join(OUTPUT_DIR, filename)
    df.to_json(filepath, orient='records', lines=True)

    # Return the full path of the saved file
    return filepath
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
filename = 'test.jsonl'