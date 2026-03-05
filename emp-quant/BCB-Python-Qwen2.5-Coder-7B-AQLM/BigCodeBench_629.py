
import os
import time
import pandas as pd

OUTPUT_DIR = './output'

def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").
    
    Parameters:
    - dataset: A list of Pandas DataFrames to be written to the CSV file.
    - filename: The name of the output CSV file.
    - output_dir: The directory where the output CSV file will be saved.
    
    Returns:
    - None
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full path for the output file
    output_path = os.path.join(output_dir, filename)
    
    # Open the file in write mode
    with open(output_path, 'w') as file:
        for df in dataset:
            # Write the DataFrame to the file
            df.to_csv(file, index=False)
            # Write a line of hyphens to separate DataFrames
            file.write('------\n')

    # List of DataFrames
    dataset = [df1, df2]
    
    # Call the function to write the DataFrames to a CSV file
    task_func(dataset, 'output.csv')
    
    print(f"DataFrames written to 'output.csv' in '{OUTPUT_DIR}'")