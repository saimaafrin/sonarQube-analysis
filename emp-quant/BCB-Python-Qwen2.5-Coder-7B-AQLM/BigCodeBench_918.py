
import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    """
    Replaces all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame containing string cells with acronyms.
    mapping (dict): A dictionary where keys are acronyms and values are their full words.
    
    Returns:
    pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    """
    # Create a regex pattern to match any acronym in the mapping dictionary
    acronym_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, mapping.keys())) + r')\b')
    
    # Function to replace acronyms with their full words
    def replace_acronyms(text):
        return acronym_pattern.sub(lambda match: mapping[match.group()], text)
    
    # Apply the replacement function to all string cells in the DataFrame
    for column in data.select_dtypes(include=[object]):
        data[column] = data[column].apply(replace_acronyms)
    
    return data

    # Mapping of acronyms to their full words
    mapping = {
        'acronym': 'acronym full word',
        'another': 'another full word'
    }
    
    # Replace acronyms in the DataFrame
    result = task_func(data, mapping)
    
    # Print the result
    print(result)