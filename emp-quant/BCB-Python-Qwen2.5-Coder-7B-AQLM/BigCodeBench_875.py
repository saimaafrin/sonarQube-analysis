
import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Determine the maximum length of the tuples
    max_len = max(len(row) for row in data)
    
    # Create a list of lists to hold the data
    rows = []
    for row in data:
        # Extend the row with None to match the maximum length
        row = list(row) + [None] * (max_len - len(row))
        rows.append(row)
    
    # Create the DataFrame
    df = pd.DataFrame(rows, columns=columns)
    
    # Fill missing numeric values with random data if fill_missing is True
    if fill_missing:
        for col in df.select_dtypes(include=[float, int]).columns:
            df[col].fillna(random.uniform(num_range[0], num_range[1]), inplace=True)
    
    return df