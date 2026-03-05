import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries to hold the data
    data_list = []
    for row in data:
        row_dict = {}
        for i, value in enumerate(row):
            if i < len(columns):
                row_dict[columns[i]] = value
        data_list.append(row_dict)
    
    # Create the DataFrame
    df = pd.DataFrame(data_list)
    
    # Fill missing values
    if fill_missing:
        for column in df.columns:
            if df[column].dtype == 'float64':
                df[column].fillna(random.uniform(num_range[0], num_range[1]), inplace=True)
            elif df[column].dtype == 'int64':
                df[column].fillna(random.randint(num_range[0], num_range[1]), inplace=True)
            else:
                df[column].fillna(None, inplace=True)
    
    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]