import os
import time
import pandas as pd
OUTPUT_DIR = './output'
def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a full file path
    file_path = os.path.join(output_dir, filename)
    
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Iterate over each DataFrame in the dataset
        for df in dataset:
            # Write the DataFrame to the file
            df.to_csv(file, index=False)
            # Write a line of hyphens after each DataFrame
            file.write('------\n')