
import pandas as pd
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The name of the file to save.
        output_dir (str, optional): The directory to save the file in. Defaults to './output'.

    Returns:
        str: The full file path where the DataFrame is saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    df.to_json(filepath, orient='records')
    return filepath