import csv
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a CSV file in a specified directory.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        filename (str): The name of the file to save.
        output_dir (str, optional): The directory to save the file in. Defaults to './output'.

    Returns:
        str: The absolute path of the saved CSV file.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the DataFrame to a CSV file
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)

    # Return the absolute path of the saved CSV file
    return os.path.abspath(filepath)
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [24, 36, 42]})
filename = 'data.csv'
output_dir = 'output'