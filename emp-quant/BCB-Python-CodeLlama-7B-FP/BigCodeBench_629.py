import os
import time
OUTPUT_DIR = './output'
def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").
    """
    # Create a list of DataFrames
    dataframes = [dataset]

    # Create a list of filenames
    filenames = [filename]

    # Create a list of output directories
    output_dirs = [output_dir]

    # Create a list of file paths
    file_paths = [os.path.join(output_dir, filename) for output_dir, filename in zip(output_dirs, filenames)]

    # Write each DataFrame to a separate CSV file
    for dataframe, file_path in zip(dataframes, file_paths):
        dataframe.to_csv(file_path, index=False)

    # Add a line of hyphens to separate each DataFrame
    with open(file_path, 'a') as f:
        f.write('------\n')