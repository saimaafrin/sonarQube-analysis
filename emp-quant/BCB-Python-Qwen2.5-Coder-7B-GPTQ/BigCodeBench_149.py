import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements.
    This function can optionally include an index column for each row in the DataFrame.
    
    :param elements: List of strings to process.
    :param include_index: Boolean indicating whether to include an index column.
    :return: pandas DataFrame with columns for elements and their respective character counts.
    """
    # Create a list of tuples with element and its count
    data = [(element, len(element)) for element in elements]
    
    # Define the columns based on the include_index parameter
    columns = ['Index', 'Element', 'Count'] if include_index else DEFAULT_COLUMNS
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # If include_index is True, set the 'Index' column as the index of the DataFrame
    if include_index:
        df.set_index('Index', inplace=True)
    
    return df
elements = ["apple", "banana", "cherry"]