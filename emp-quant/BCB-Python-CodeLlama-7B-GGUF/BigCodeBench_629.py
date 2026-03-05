
import os
import time

OUTPUT_DIR = './output'

def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    # Create a new CSV file in the output directory
    csv_file = os.path.join(output_dir, filename)
    with open(csv_file, 'w') as f:
        # Write the header row
        f.write('Name,Age,Gender\n')
        # Write the data rows
        for row in dataset:
            f.write(f'{row["Name"]},{row["Age"]},{row["Gender"]}\n')
        # Add a line of hyphens to separate the DataFrames
        f.write('------\n')

# Call the function with the two datasets
task_func(dataset1, 'dataset1.csv')
task_func(dataset2, 'dataset2.csv')