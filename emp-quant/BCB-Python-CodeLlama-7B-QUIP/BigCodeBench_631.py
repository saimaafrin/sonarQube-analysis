
import csv
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Get the absolute path of the saved CSV file
    file_path = os.path.join(output_dir, filename)
    # Save the DataFrame to the CSV file
    df.to_csv(file_path, index=False)
    return file_path