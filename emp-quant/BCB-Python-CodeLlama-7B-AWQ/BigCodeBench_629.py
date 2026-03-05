import os
import time
OUTPUT_DIR = './output'
def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").
    The function should output with:
        None: The function writes the DataFrames to a CSV file but does not return any value.
    """
    # Check if the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a CSV file with the given filename
    with open(os.path.join(output_dir, filename), 'w') as f:
        # Write the DataFrames to the CSV file
        for df in dataset:
            f.write('------\n')
            df.to_csv(f, index=False)