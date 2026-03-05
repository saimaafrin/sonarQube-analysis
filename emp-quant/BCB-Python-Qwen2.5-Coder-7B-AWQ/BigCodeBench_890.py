import os
import random
import pandas as pd
def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    """
    Randomly select one of the provided csv_files and select a certain number of records from the file at random.
    The selected records are returned in a DataFrame. The name of the selected csv_file is also returned.
    If the csv_file is empty return an empty DataFrame.
    
    :param data_dir: str - The directory containing the csv files.
    :param csv_files: list - A list of csv file names to choose from.
    :param seed: int - The seed for the random number generator.
    :return: tuple - A tuple containing the name of the randomly selected file and a pandas DataFrame with the selected rows.
    """
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Select a random csv file
    selected_file = random.choice(csv_files)
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file is empty
    if not os.path.getsize(file_path):
        return selected_file, pd.DataFrame()
    
    # Read the csv file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Select a random sample of rows
    sample_size = min(10, len(df))  # Limit to 10 rows or the number of rows in the file, whichever is smaller
    sampled_df = df.sample(n=sample_size, random_state=seed)
    
    return selected_file, sampled_df