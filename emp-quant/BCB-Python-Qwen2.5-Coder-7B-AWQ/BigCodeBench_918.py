import pandas as pd
import re
def task_func(data, mapping):
    """
    Replaces all acronyms in a DataFrame with their full words according to a provided dictionary.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing string cells with acronyms.
    mapping (dict): A dictionary where keys are acronyms and values are their full words.

    Returns:
    pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    """
    # Create a regex pattern to match any acronym in the mapping
    acronym_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, mapping.keys())) + r')\b')

    # Function to replace acronyms with their full words
    def replace_acronym(match):
        return mapping[match.group(0)]

    # Apply the replacement to each string cell in the DataFrame
    replaced_data = data.applymap(lambda x: acronym_pattern.sub(replace_acronym, x) if isinstance(x, str) else x)

    return replaced_data