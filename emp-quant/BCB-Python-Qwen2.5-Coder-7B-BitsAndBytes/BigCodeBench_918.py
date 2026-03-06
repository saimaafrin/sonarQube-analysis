
import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    """
    Replaces all acronyms in a DataFrame with their full words according to a provided dictionary.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing text with acronyms.
    mapping (dict): A dictionary where keys are acronyms and values are their full words.

    Returns:
    pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    """
    # Create a regex pattern from the mapping keys
    acronym_pattern = re.compile(r'\b(' + '|'.join(re.escape(acro) for acro in mapping.keys()) + r')\b')

    # Define a replacement function
    def replace_acronym(match):
        return mapping[match.group(0)]

    # Apply the replacement function to each element in the DataFrame
    result_df = data.applymap(lambda x: acronym_pattern.sub(replace_acronym, str(x)) if isinstance(x, str) else x)

    return result_df

    # Mapping of acronyms to full words
    acronym_mapping = {
        'API': 'Application Programming Interface',
        'AI': 'Artificial Intelligence'
    }

    # Replace acronyms in the DataFrame
    result = task_func(df, acronym_mapping)
    print(result)