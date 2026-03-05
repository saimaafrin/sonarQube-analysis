import math
import pandas as pd
def task_func(tuples_list):
    """
    Convert a list of tuples into a Pandas DataFrame with math.sin applied to each number.

    Parameters:
    tuples_list (list of tuples): A list where each element is a tuple of numbers.

    Returns:
    df (DataFrame): A pandas DataFrame. Each row of df corresponds to a tuple from tuples_list, with the values being the sine of the original values in the tuple.
    """
    # Apply math.sin to each element in the tuples
    transformed_data = [[math.sin(num) for num in tup] for tup in tuples_list]
    
    # Create a DataFrame from the transformed data
    df = pd.DataFrame(transformed_data)
    
    return df
tuples_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]