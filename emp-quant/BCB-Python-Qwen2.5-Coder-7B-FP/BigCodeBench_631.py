import pandas as pd
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full path for the CSV file
    csv_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(csv_path)