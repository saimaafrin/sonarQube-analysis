
import csv
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the DataFrame to a CSV file
    csv_file = os.path.join(output_dir, filename)
    df.to_csv(csv_file, index=False)

    # Return the absolute path of the saved CSV file
    return os.path.abspath(csv_file)