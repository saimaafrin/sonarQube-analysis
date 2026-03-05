
import re
import pandas as pd
import numpy as np
# Constants
DATA_PATTERN = r'>\d+\.\d+<'
def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    
    The function searches each cell for occurrences of the regex pattern '>number<number>'
    (e.g., '>1.23<') and replaces the cell content with the extracted numeric value.
    If no match is found, the cell is replaced with NaN.
    
    Parameters:
    dataframe (pd.DataFrame): The input DataFrame to process.
    data_pattern (str): The regex pattern to search for.
    
    Returns:
    pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    """
    # Define a function to extract the numeric value from a string
    def extract_number(match):
        return float(match.group(1))
    
    # Apply the regex pattern to each cell in the DataFrame
    for col in dataframe.columns:
        dataframe[col] = dataframe[col].apply(lambda x: extract_number(re.search(data_pattern, str(x))) if re.search(data_pattern, str(x)) else np.nan)
    
    return dataframe