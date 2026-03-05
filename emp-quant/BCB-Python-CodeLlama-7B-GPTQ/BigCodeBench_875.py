import pandas as pd
import random
def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    """
    Create a Pandas DataFrame from a list of tuples, each representing a row.
    Tuples of unequal lengths are allowed, and missing elements are filled with None.
    Optionally, missing numeric values can be filled with random data.
    """
    # Create a list of lists to store the data
    data_list = []

    # Iterate over the input data
    for row in data:
        # Create a list to store the row data
        row_data = []

        # Iterate over the columns
        for i, column in enumerate(columns):
            # Check if the column is missing
            if i >= len(row):
                # Fill the missing column with None
                row_data.append(None)
            else:
                # Check if the column is numeric
                if isinstance(row[i], (int, float)):
                    # Fill the numeric column with random data
                    row_data.append(random.randint(num_range[0], num_range[1]))
                else:
                    # Fill the non-numeric column with the corresponding value
                    row_data.append(row[i])

        # Add the row data to the data list
        data_list.append(row_data)

    # Create the DataFrame
    df = pd.DataFrame(data_list, columns=columns)

    # Fill missing elements with None
    if fill_missing:
        df = df.fillna(None)

    # Return the DataFrame
    return df
data = [('Mango', 20), ('Apple', ), ('Banana', )]