import csv
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a CSV file in a specified directory.
    This function takes a Pandas DataFrame and a filename as input and saves the DataFrame to a CSV file.
    The CSV file will be saved in the 'data' directory relative to the parent directory of this script.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the DataFrame to a CSV file
    csv_file = os.path.join(output_dir, filename)
    df.to_csv(csv_file, index=False)

    # Return the absolute path of the saved CSV file
    return os.path.abspath(csv_file)
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35]})
filename = 'data.csv'
output_dir = './output'