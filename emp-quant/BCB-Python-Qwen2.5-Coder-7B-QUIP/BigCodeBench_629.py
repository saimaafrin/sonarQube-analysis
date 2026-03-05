
import os
import time
OUTPUT_DIR = './output'

def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the path for the output CSV file
    output_file = os.path.join(output_dir, filename)

    # Open the file in write mode
    with open(output_file, 'w') as file:
        for i, df in enumerate(dataset):
            # Write the DataFrame to the file
            df.to_csv(file, index=False, header=i == 0)
            # Write a separator line after each DataFrame
            if i < len(dataset) - 1:
                file.write('------\n')

    return None