import pandas as pd
import re
def task_func(data, mapping):
    """
    Replace all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Requirements:
    - pandas
    - re

    Parameters:
    - data (dict): A dictionary where keys are column names and values are lists of strings.
    - mapping (dict): A dictionary where keys are acronyms and values are the full words.
    
    Returns:
    - pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    
    Examples:
    >>> data = {'text': ['NASA is great', 'I live in the USA']}
    >>> mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
    >>> print(task_func(data, mapping))
                                                    text
    0  National Aeronautics and Space Administration ...
    1             I live in the United States of America
    """
    # Create a new DataFrame
    df = pd.DataFrame()
    
    # Iterate over the keys in the dictionary
    for key in mapping.keys():
        # Replace all acronyms in the DataFrame with their full words
        data[key] = data[key].apply(lambda x: re.sub(key, mapping[key], x))
    
    # Add the new columns to the DataFrame
    df = df.join(data)
    
    # Return the DataFrame
    return df
data = {'text': ['NASA is great', 'I live in the USA']}
mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}