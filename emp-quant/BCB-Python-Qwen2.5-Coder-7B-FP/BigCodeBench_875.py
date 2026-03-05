import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries to hold the data
    rows = []
    for row_data in data:
        row_dict = {columns[i]: value for i, value in enumerate(row_data)}
        # Fill missing values with None or random data
        for col in columns:
            if col not in row_dict:
                if fill_missing:
                    row_dict[col] = random.randint(num_range[0], num_range[1])
                else:
                    row_dict[col] = None
        rows.append(row_dict)
    
    # Create the DataFrame
    df = pd.DataFrame(rows, columns=columns)
    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]