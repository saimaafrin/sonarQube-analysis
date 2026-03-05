import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    """
    Create a Pandas DataFrame from a list of tuples, each representing a row.
    Tuples of unequal lengths are allowed, and missing elements are filled with None.
    Optionally, missing numeric values can be filled with random data.
    """
    # Create a list of lists from the input data
    data_list = [list(row) for row in data]

    # Create a list of column names
    column_names = columns

    # Create a list of data types for each column
    data_types = [None] * len(column_names)

    # Fill in missing values with None or random data
    if fill_missing:
        for i, column in enumerate(column_names):
            if data_types[i] == int:
                data_list = [random.randint(num_range[0], num_range[1]) if value is None else value for value in data_list]
            elif data_types[i] == float:
                data_list = [random.uniform(num_range[0], num_range[1]) if value is None else value for value in data_list]
            else:
                data_list = [value if value is not None else None for value in data_list]

    # Create a Pandas DataFrame from the list of lists
    df = pd.DataFrame(data_list, columns=column_names)

    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]