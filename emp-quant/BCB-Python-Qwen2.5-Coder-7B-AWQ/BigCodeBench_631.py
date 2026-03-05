import csv
import os
from pathlib import Path
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Construct the full path for the CSV file
    full_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a CSV file
    df.to_csv(full_path, index=False)
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(full_path)