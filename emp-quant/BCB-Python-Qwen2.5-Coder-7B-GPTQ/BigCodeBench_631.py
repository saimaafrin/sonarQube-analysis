import csv
import os
import pandas as pd
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full path for the CSV file
    file_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(file_path)