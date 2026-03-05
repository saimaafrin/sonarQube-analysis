
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Extract the column of interest
    column = df[column_name]

    # Create a list of all indices where the pattern is found
    indices = [i for i, x in enumerate(column) if re.search(pattern, x)]

    # If a sample size is specified, generate a random sample of indices
    if sample_size:
        random.seed(seed)
        indices = random.sample(indices, sample_size)

    # Return a DataFrame with either all the matches or a random sample of them
    return df.iloc[indices]