import pandas as pd
import re
def task_func(data, mapping):
    """
    Replace all acronyms in a DataFrame with their full words according to a provided dictionary.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to be processed.
    mapping : dict
        A dictionary mapping acronyms to their full words.

    Returns
    -------
    pd.DataFrame
        A DataFrame where all acronyms in string cells have been replaced with their full words.
    """
    # Create a regular expression pattern to match acronyms
    pattern = r'\b(' + '|'.join(mapping.keys()) + r')\b'

    # Replace acronyms in each string cell
    for col in data.columns:
        data[col] = data[col].str.replace(pattern, lambda x: mapping[x.group()])

    return data
data = pd.DataFrame({'A': ['ACME', 'ABC', 'XYZ', 'XYZ'],
                     'B': ['XYZ', 'ABC', 'ACME', 'XYZ']})
mapping = {'ACME': 'A Company Made Extraordinary',
           'ABC': 'A B C',
           'XYZ': 'X Y Z'}