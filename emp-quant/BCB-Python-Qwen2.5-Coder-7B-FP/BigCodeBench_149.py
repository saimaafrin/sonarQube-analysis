import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements.
    
    Parameters:
    elements (list): A list of string elements.
    include_index (bool): If True, includes an 'Index' column for each row in the DataFrame.
    
    Returns:
    DataFrame: A pandas DataFrame with columns for elements and their respective character counts.
    """
    # Create a list of dictionaries to hold the data
    data = []
    for index, element in enumerate(elements):
        data.append({'Element': element, 'Count': len(element)})
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    # Add an 'Index' column if requested
    if include_index:
        df.insert(0, 'Index', range(len(df)))
    
    # Reorder columns if 'Index' is included
    if include_index:
        df = df[DEFAULT_COLUMNS + ['Index']]
    else:
        df = df[DEFAULT_COLUMNS]
    
    return df
elements = ['apple', 'banana', 'cherry']