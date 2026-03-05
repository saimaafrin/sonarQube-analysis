
import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    # Create a list of tuples with elements and their counts
    data = [(element, len(element)) for element in elements]
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=DEFAULT_COLUMNS)
    
    # If include_index is True, add an 'Index' column
    if include_index:
        df['Index'] = np.arange(len(df))
    
    # Reorder the columns to match the desired output
    if include_index:
        df = df[['Index', 'Element', 'Count']]
    
    return df