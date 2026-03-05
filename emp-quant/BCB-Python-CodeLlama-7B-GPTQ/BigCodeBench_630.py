import pandas as pd
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.
    """
    # Check if the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the DataFrame as a JSON file
    filepath = os.path.join(output_dir, filename)
    df.to_json(filepath, orient='records')

    # Return the full file path where the DataFrame is saved
    return filepath
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35]})
filename = 'data.json'
output_dir = './output'