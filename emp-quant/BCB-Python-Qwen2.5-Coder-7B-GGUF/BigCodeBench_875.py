
import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries to hold the data
    data_list = []
    for row in data:
        row_dict = {columns[i]: row[i] if i < len(row) else None for i in range(len(columns))}
        data_list.append(row_dict)
    
    # Create the DataFrame
    df = pd.DataFrame(data_list)
    
    # Fill missing numeric values with random data if required
    if fill_missing:
        for column in columns:
            if df[column].dtype == 'float64' or df[column].dtype == 'int64':
                df[column] = df[column].fillna(random.uniform(num_range[0], num_range[1]))
    
    return df