
import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    # Create a dictionary to store the counts of each element
    counts = {element: len(element) for element in elements}
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(list(counts.items()), columns=DEFAULT_COLUMNS)
    
    # If include_index is True, add an 'Index' column
    if include_index:
        df.insert(0, 'Index', np.arange(len(df)))
    
    return df