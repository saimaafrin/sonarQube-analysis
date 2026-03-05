
import csv
import os
OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the absolute path for the output file
    output_path = os.path.join(output_dir, filename)

    # Save the DataFrame to the CSV file
    df.to_csv(output_path, index=False)

    # Return the absolute path of the saved CSV file
    return output_path