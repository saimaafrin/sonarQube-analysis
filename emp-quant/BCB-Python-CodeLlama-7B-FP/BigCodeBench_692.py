import math
import pandas as pd
def task_func(tuples_list):
    """
    Given a list of tuples, turn them into a Pandas DataFrame with math.sin applied to each number.
    The function should output with:
        df (DataFrame): A pandas DataFrame. Each row of df corresponds to a tuple from tuples_list, with the values being the sine of the original values in the tuple.
    """
    # Create a list of lists to store the sine values
    sine_values = []

    # Iterate over the tuples in the list
    for tuple in tuples_list:
        # Create a list to store the sine values for this tuple
        sine_values_for_tuple = []

        # Iterate over the values in the tuple
        for value in tuple:
            # Calculate the sine of the value and append it to the list
            sine_values_for_tuple.append(math.sin(value))

        # Add the list of sine values for this tuple to the list of lists
        sine_values.append(sine_values_for_tuple)

    # Create the DataFrame
    df = pd.DataFrame(sine_values, columns=["Sine"])

    return df
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]