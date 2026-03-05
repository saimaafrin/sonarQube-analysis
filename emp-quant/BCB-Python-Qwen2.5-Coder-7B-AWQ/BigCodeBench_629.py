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
    with open(file_path, 'w', newline='') as file:
        for i, df in enumerate(dataset):
            # Convert the DataFrame to a CSV string
            csv_str = df.to_csv(index=False)
            
            # Write the CSV string to the file
            file.write(csv_str)
            
            # Write a line of hyphens after each DataFrame
            if i < len(dataset) - 1:
                file.write('------\n')