
import csv
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a CSV file in a specified directory.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        filename (str): The filename to use for the saved CSV file.
        output_dir (str, optional): The directory to save the CSV file to. Defaults to './output'.

    Returns:
        str: The absolute path of the saved CSV file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)

    return filepath