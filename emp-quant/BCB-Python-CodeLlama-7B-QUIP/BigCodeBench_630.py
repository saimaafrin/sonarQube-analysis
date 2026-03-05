
import pandas as pd
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Save the DataFrame to a JSON file
    df.to_json(os.path.join(output_dir, filename), orient='records')
    # Return the full file path where the DataFrame is saved
    return os.path.join(output_dir, filename)