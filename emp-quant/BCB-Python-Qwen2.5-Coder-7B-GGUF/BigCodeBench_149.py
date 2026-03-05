
import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    # Create a list to store the data for the DataFrame
    data = []
    
    # Iterate over the elements and count the characters
    for index, element in enumerate(elements):
        count = len(element)
        data.append([index, element, count] if include_index else [element, count])
    
    # Create the DataFrame with the appropriate columns
    columns = ['Index', 'Element', 'Count'] if include_index else DEFAULT_COLUMNS
    df = pd.DataFrame(data, columns=columns)
    
    return df