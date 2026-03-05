import os
import time
OUTPUT_DIR = './output'
def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    """Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").

    Args:
        dataset (list of Pandas DataFrames): The list of DataFrames to write to the CSV file.
        filename (str): The name of the CSV file to write to.
        output_dir (str, optional): The directory to write the CSV file to. Defaults to './output'.

    Returns:
        None: The function writes the DataFrames to a CSV file but does not return any value.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the CSV file for writing
    with open(os.path.join(output_dir, filename), 'w') as f:
        # Write the DataFrames to the CSV file, separated by a line of hyphens
        for df in dataset:
            f.write('------\n')
            df.to_csv(f, index=False)