
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Extract the column with the specified name
    column = df[column_name]

    # Create a list of indices that correspond to the rows with matches
    matches = [i for i, row in enumerate(column) if pattern.search(row)]

    # If sample_size is not None, create a random sample of indices
    if sample_size:
        random_indices = random.sample(matches, sample_size)
        matches = random_indices

    # Return the DataFrame with either all the matches or a random sample
    return df.iloc[matches]