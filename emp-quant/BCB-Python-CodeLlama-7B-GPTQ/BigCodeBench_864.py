import pandas as pd
import numpy as np
def task_func(fruit_data):
    """
    Calculate and return the total and average counts for each type of fruit.
    This function takes a list of tuples, each containing a fruit name and its count, then calculates the total count and the average count for each type of fruit.
    The results are returned as a pandas DataFrame with each row representing a different fruit.
    If fruit_data is an empty list, an empty dataFrame is returned.
    """
    # Check if fruit_data is an empty list
    if not fruit_data:
        return pd.DataFrame()

    # Create a dictionary to store the total and average counts for each fruit
    fruit_counts = {}

    # Iterate over the fruit data and calculate the total and average counts for each fruit
    for fruit, count in fruit_data:
        if fruit not in fruit_counts:
            fruit_counts[fruit] = {
                'Total Count': count,
                'Average Count': count
            }
        else:
            fruit_counts[fruit]['Total Count'] += count
            fruit_counts[fruit]['Average Count'] = (
                fruit_counts[fruit]['Total Count'] / len(fruit_data)
            )

    # Create a pandas DataFrame from the fruit counts dictionary
    df = pd.DataFrame.from_dict(fruit_counts, orient='index')

    # Sort the DataFrame by fruit name
    df.sort_index(inplace=True)

    return df
fruit = [('apple', 1), ('orange', 25), ('apple', 111)]