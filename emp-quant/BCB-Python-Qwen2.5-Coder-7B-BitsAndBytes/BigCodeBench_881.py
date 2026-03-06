
import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Find rows where the column matches the regex pattern
    matching_rows = df[df[column_name].str.contains(pattern)]
    
    if sample_size is not None:
        # Set the random seed for reproducibility
        random.seed(seed)
        
        # Generate a random list of indices to sample from the matching rows
        sampled_indices = random.sample(range(len(matching_rows)), min(sample_size, len(matching_rows)))
        
        # Select the sampled rows
        result_df = matching_rows.iloc[sampled_indices]
    else:
        result_df = matching_rows
    
    return result_df