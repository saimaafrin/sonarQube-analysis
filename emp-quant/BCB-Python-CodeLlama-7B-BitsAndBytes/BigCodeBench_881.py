
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Extract the column of interest
    column = df[column_name]

    # Create a list of indices for the random sample
    if sample_size is not None:
        random.seed(seed)
        indices = random.sample(range(len(column)), sample_size)
    else:
        indices = range(len(column))

    # Filter the DataFrame using the indices
    filtered_df = df.iloc[indices]

    # Return the filtered DataFrame
    return filtered_df