
import os
import random
import pandas as pd

def task_func(data_dir, csv_files=['file1.csv', 'file2.csv', 'file3.csv'], seed=None):
    # Set the seed for random selection
    if seed is not None:
        random.seed(seed)

    # Select a random file from the list
    selected_file = random.choice(csv_files)

    # Construct the full path to the selected file
    file_path = os.path.join(data_dir, selected_file)

    # Check if the file exists
    if not os.path.exists(file_path):
        return (selected_file, pd.DataFrame())

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check if the DataFrame is empty
    if df.empty:
        return (selected_file, pd.DataFrame())

    # Select a random number of records from the DataFrame
    num_records = random.randint(1, len(df))
    selected_records = df.sample(n=num_records, random_state=seed)

    # Return the selected file name and the selected records as a tuple
    return (selected_file, selected_records)