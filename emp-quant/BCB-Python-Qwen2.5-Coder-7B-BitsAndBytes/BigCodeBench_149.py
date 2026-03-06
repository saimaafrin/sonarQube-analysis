
import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements.
    
    Parameters:
    - elements (list): A list of strings to process.
    - include_index (bool): If True, includes an 'Index' column in the DataFrame.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns for elements and their respective character counts.
                 Includes an 'Index' column if requested.
    """
    # Create a dictionary to store the element counts
    data_dict = {'Element': elements, 'Count': [len(element) for element in elements]}
    
    # If include_index is True, add an 'Index' column
    if include_index:
        data_dict['Index'] = range(len(elements))
    
    # Create the DataFrame
    df = pd.DataFrame(data_dict)
    
    # Reorder columns if include_index is True
    if include_index:
        df = df[['Index', 'Element', 'Count']]
    
    return df

df_without_index = task_func(elements, include_index=False)
print("\nDataFrame without Index:")
print(df_without_index)