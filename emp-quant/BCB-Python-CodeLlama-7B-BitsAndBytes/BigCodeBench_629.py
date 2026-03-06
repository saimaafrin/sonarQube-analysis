
import os
import time
OUTPUT_DIR = './output'

def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Create a new CSV file in the output directory
    csv_file = os.path.join(output_dir, filename)
    with open(csv_file, 'w') as f:
        # Write the header row
        f.write('------\n')
        f.write(dataset.columns.to_csv(header=True, index=False))
        f.write('\n')
        # Write the data rows
        for _, row in dataset.iterrows():
            f.write(row.to_csv(header=False, index=False))
            f.write('\n')
        # Write a line of hyphens to separate the DataFrames
        f.write('------\n')
    return None