
import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a list to hold the rows for the DataFrame
    rows = []
    
    # Iterate over the data and create rows
    for item in data:
        # Calculate the number of missing elements
        num_missing = len(columns) - len(item)
        
        # If fill_missing is True, fill missing elements with random numbers
        if fill_missing:
            missing_values = [random.randint(num_range[0], num_range[1]) for _ in range(num_missing)]
        else:
            missing_values = [None] * num_missing
        
        # Combine the existing item with the missing values
        row = list(item) + missing_values
        
        # Append the row to the list
        rows.append(row)
    
    # Create the DataFrame
    df = pd.DataFrame(rows, columns=columns)
    
    return df