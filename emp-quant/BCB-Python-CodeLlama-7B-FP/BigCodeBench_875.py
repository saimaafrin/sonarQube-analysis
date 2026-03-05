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

    # Fill missing elements with None or random data
    if fill_missing:
        for i, row in enumerate(data_list):
            for j, element in enumerate(row):
                if element is None:
                    if data_types[j] == int:
                        data_list[i][j] = random.randint(num_range[0], num_range[1])
                    elif data_types[j] == float:
                        data_list[i][j] = random.uniform(num_range[0], num_range[1])
                    else:
                        data_list[i][j] = None

    # Create a Pandas DataFrame from the list of lists
    df = pd.DataFrame(data_list, columns=column_names)

    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]