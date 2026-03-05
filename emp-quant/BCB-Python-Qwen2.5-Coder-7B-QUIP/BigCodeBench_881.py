
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Find all rows that match the regex pattern in the specified column
    matching_rows = df[df[column_name].str.contains(pattern, na=False)]
    
    # If sample_size is specified, randomly sample from the matching rows
    if sample_size is not None:
        if sample_size > len(matching_rows):
            raise ValueError("Sample size is larger than the number of matching rows")
        matching_rows = matching_rows.sample(n=sample_size, random_state=seed)
    
    # Return the DataFrame with matching rows
    return matching_rows