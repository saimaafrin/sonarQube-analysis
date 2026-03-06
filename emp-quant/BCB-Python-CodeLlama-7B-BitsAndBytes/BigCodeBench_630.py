
import pandas as pd
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Save the DataFrame to a JSON file in the specified directory
    filepath = os.path.join(output_dir, filename)
    df.to_json(filepath, orient='records')
    return filepath