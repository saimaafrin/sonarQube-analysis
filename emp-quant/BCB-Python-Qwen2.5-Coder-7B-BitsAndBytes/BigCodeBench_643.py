
import re
import pandas as pd
import numpy as np

# Constants
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
    # Define a function to extract numbers using regex
    def extract_number(match):
        return float(match.group(0)[1:-1])
    
    # Apply the extraction function to each element in the DataFrame
    result_df = dataframe.applymap(lambda x: re.sub(data_pattern, extract_number, str(x)) if isinstance(x, str) else x)
    
    # Convert the string representations of numbers back to floats
    result_df = result_df.apply(pd.to_numeric, errors='coerce')
    
    return result_df