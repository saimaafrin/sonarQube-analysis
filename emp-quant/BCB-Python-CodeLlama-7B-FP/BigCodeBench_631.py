import csv
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a CSV file in a specified directory.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        filename (str): The name of the CSV file to save.
        output_dir (str, optional): The directory to save the CSV file in. Defaults to './output'.

    Returns:
        str: The absolute path of the saved CSV file.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the DataFrame to a CSV file
    csv_file = os.path.join(output_dir, filename)
    df.to_csv(csv_file, index=False)

    # Return the absolute path of the saved CSV file
    return os.path.abspath(csv_file)
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
filename = 'test.csv'
output_dir = './output'