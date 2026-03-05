
import pandas as pd
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    filename (str): The name of the file to save the DataFrame as.
    output_dir (str): The directory to save the file in. Defaults to OUTPUT_DIR.

    Returns:
    str: The full file path where the DataFrame is saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the full file path
    file_path = os.path.join(output_dir, filename)

    # Save the DataFrame to the JSON file
    df.to_json(file_path, orient='index')

    # Return the full file path
    return file_path