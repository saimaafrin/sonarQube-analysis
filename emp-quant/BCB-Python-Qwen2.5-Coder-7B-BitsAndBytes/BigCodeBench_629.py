
import os
import pandas as pd

OUTPUT_DIR = './output'

def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create the full path for the output file
    filepath = os.path.join(output_dir, filename)

    # Open the file in write mode
    with open(filepath, 'w', newline='') as file:
        for i, df in enumerate(dataset):
            # Convert the DataFrame to a string and write it to the file
            df.to_csv(file, index=False)
            # Write a line of hyphens after each DataFrame except the last one
            if i < len(dataset) - 1:
                file.write('------\n')

    # Call the function with the example data
    task_func(dataset, 'output.csv')