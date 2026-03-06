
import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements.

    Parameters
    ----------
    elements : list
        A list of strings to be counted.
    include_index : bool, default False
        Whether to include an 'Index' column in the DataFrame.

    Returns
    -------
    DataFrame
        A pandas DataFrame with columns for elements and their respective character counts.
    """
    # Create a list of tuples containing the element and its count
    counts = [(element, len(element)) for element in elements]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(counts, columns=DEFAULT_COLUMNS)

    # Add an 'Index' column if requested
    if include_index:
        df['Index'] = np.arange(len(df))

    return df