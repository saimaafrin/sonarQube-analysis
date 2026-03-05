import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries to hold the data
    rows = []
    for row in data:
        # Create a dictionary for each row with default values as None
        row_dict = {col: None for col in columns}
        # Fill the dictionary with the data from the tuple
        for i, value in enumerate(row):
            if i < len(columns):
                row_dict[columns[i]] = value
                if isinstance(value, (int, float)) and fill_missing:
                    row_dict[columns[i]] = random.randint(num_range[0], num_range[1])
        rows.append(row_dict)
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(rows)
    
    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]