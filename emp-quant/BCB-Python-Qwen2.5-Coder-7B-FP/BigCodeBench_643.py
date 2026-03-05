import re
import pandas as pd
import numpy as np
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extracts numeric data from a Pandas DataFrame based on a specific pattern.
    
    Args:
    dataframe (pd.DataFrame): The input DataFrame to process.
    data_pattern (str): The regex pattern to search for numeric data.
    
    Returns:
    pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    """
    # Define a function to extract the numeric value from a string
    def extract_number(match):
        return float(match.group(0)[1:-1])
    
    # Apply the regex pattern to each element in the DataFrame
    modified_df = dataframe.applymap(lambda x: re.sub(data_pattern, extract_number, str(x)) if isinstance(x, str) else x)
    
    # Convert the extracted strings to floats and replace non-numeric values with NaN
    modified_df = modified_df.applymap(lambda x: float(x) if isinstance(x, str) and re.match(r'^-?\d+\.\d+$', x) else np.nan)
    
    return modified_df