
import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    # Create a list of tuples containing the element and its character count
    element_counts = [(element, len(element)) for element in elements]
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(element_counts, columns=DEFAULT_COLUMNS)
    
    # Add an 'Index' column if requested
    if include_index:
        df['Index'] = range(1, len(df) + 1)
    
    return df