import math
import pandas as pd
def task_func(tuples_list):
    """
    Given a list of tuples, turn them into a Pandas DataFrame with math.sin applied to each number.
    The function should output with:
        df (DataFrame): A pandas DataFrame. Each row of df corresponds to a tuple from tuples_list, with the values being the sine of the original values in the tuple.
    """
    # Create a list of lists to store the data
    data = []

    # Iterate over the tuples in the list
    for tuple in tuples_list:
        # Create a list to store the data for this tuple
        tuple_data = []

        # Iterate over the values in the tuple
        for value in tuple:
            # Apply math.sin to each value and add it to the list
            tuple_data.append(math.sin(value))

        # Add the list to the data list
        data.append(tuple_data)

    # Create the DataFrame
    df = pd.DataFrame(data, columns=['sin_value'])

    return df
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]