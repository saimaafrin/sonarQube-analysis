
import os
import time
OUTPUT_DIR = './output'
def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Write the DataFrame to a CSV file
    dataset.to_csv(os.path.join(output_dir, filename), index=False, sep='\t')
    # Add a line of hyphens to separate the DataFrames
    with open(os.path.join(output_dir, filename), 'a') as f:
        f.write('------\n')