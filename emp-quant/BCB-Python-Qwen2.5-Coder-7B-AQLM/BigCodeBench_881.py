
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Find all rows where the specified column matches the regex pattern
    matches = df[df[column_name].str.contains(pattern, na=False)]
    
    # If sample_size is specified and greater than 0, randomly sample the matches
    if sample_size is not None and sample_size > 0:
        if sample_size > len(matches):
            sample_size = len(matches)
        sample_indices = random.sample(range(len(matches)), sample_size)
        matches = matches.iloc[sample_indices]
    
    return matches