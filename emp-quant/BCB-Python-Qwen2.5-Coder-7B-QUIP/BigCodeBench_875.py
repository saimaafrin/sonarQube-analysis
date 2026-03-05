
import pandas as pd
import random

def task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Create a list of dictionaries to hold the data
    data_list = []

    # Iterate over the tuples in the input data
    for row in data:
        # Create a dictionary for each row, filling missing values with None or random data
        row_dict = {col: (random.randint(num_range[0], num_range[1]) if fill_missing and col not in row else (row[i] if i < len(row) else None)) for i, col in enumerate(columns)}
        data_list.append(row_dict)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Return the DataFrame
    return df