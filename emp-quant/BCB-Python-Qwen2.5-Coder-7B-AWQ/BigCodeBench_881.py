import pandas as pd
import random
def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Find rows where the column matches the regex pattern
    matching_rows = df[df[column_name].str.contains(regex, na=False)]
    
    # If sample_size is specified, randomly sample the rows
    if sample_size is not None:
        random.seed(seed)  # Set the seed for reproducibility
        sample_indices = random.sample(range(len(matching_rows)), sample_size)
        matching_rows = matching_rows.iloc[sample_indices]
    
    return matching_rows