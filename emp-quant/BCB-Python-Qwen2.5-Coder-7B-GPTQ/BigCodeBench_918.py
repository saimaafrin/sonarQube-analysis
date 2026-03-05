import pandas as pd
import re
def task_func(data, mapping):
    """
    Replaces all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame with string cells that may contain acronyms.
    mapping (dict): A dictionary where keys are acronyms and values are their full words.
    
    Returns:
    pd.DataFrame: A DataFrame where all acronyms have been replaced with their full words.
    """
    # Create a regex pattern to match any acronym in the mapping dictionary
    acronym_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, mapping.keys())) + r')\b')
    
    # Function to replace acronyms with their full words
    def replace_acronyms(text):
        if pd.isna(text):
            return text
        return acronym_pattern.sub(lambda match: mapping[match.group()], text)
    
    # Apply the replacement function to all string columns in the DataFrame
    for column in data.select_dtypes(include=[object]):
        data[column] = data[column].apply(replace_acronyms)
    
    return data