import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements.
    This function can optionally include an index column for each row in the DataFrame.
    Note that:
        - The order of columns in the returned DataFrame will be ['Index', 'Element', 'Count'] if the index is included.
        - The function should output with:
            - DataFrame: Returns a pandas DataFrame with columns for elements and their respective character counts.
            - Includes an 'Index' column if requested.
    """
    # Create a list of tuples containing the element and its character count
    element_counts = [(element, len(element)) for element in elements]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(element_counts, columns=DEFAULT_COLUMNS)

    # Add an 'Index' column if requested
    if include_index:
        df['Index'] = np.arange(len(df))

    return df
elements = ['apple', 'banana', 'orange']