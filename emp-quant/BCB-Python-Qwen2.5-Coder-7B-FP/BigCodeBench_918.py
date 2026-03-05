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
    # Define a function to replace acronyms in a single string
    def replace_acronyms(text):
        for acronym, full_word in mapping.items():
            text = re.sub(r'\b' + re.escape(acronym) + r'\b', full_word, text)
        return text

    # Apply the replacement function to each string cell in the DataFrame
    replaced_data = data.applymap(lambda x: replace_acronyms(x) if isinstance(x, str) else x)

    return replaced_data