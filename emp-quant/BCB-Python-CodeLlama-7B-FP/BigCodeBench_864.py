import pandas as pd
import numpy as np
def task_func(fruit_data):
    """
    Calculate and return the total and average counts for each type of fruit.
    This function takes a list of tuples, each containing a fruit name and its count, then calculates the total count and the average count for each type of fruit.
    The results are returned as a pandas DataFrame with each row representing a different fruit.
    If fruit_data is an empty list, an empty dataFrame is returned.
    """
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['Total Count', 'Average Count'])

    # Iterate over the fruit data
    for fruit, count in fruit_data:
        # Check if the fruit is already in the DataFrame
        if fruit in df.index:
            # If it is, add the count to the existing row
            df.loc[fruit, 'Total Count'] += count
            df.loc[fruit, 'Average Count'] = (df.loc[fruit, 'Total Count'] / df.loc[fruit, 'Count'])
        else:
            # If it's not, create a new row
            df = df.append({'Fruit': fruit, 'Total Count': count, 'Average Count': count}, ignore_index=True)

    # Sort the DataFrame by fruit name
    df.sort_index(inplace=True)

    return df
fruit = [('apple', 1), ('orange', 25), ('apple', 111)]