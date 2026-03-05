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
    # Create a regular expression pattern from the dictionary keys
    pattern = '|'.join(re.escape(key) for key in mapping)

    # Replace all acronyms in the DataFrame with their full words
    for col in data.columns:
        data[col] = data[col].str.replace(pattern, lambda x: mapping[x.group()])

    return data
data = pd.DataFrame({'A': ['ACME', 'ABC', 'XYZ', 'XYZ']})
mapping = {'ACME': 'Acme Inc.', 'ABC': 'ABC Company', 'XYZ': 'XYZ Corp.'}