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
    # Define a function to extract numeric data from a string
    def extract_numeric(match):
        return float(match.group(0)[1:-1])
    
    # Apply the regex pattern to each element in the DataFrame
    modified_dataframe = dataframe.applymap(lambda x: re.sub(data_pattern, extract_numeric, str(x)) if isinstance(x, str) else x)
    
    # Convert the extracted numeric strings to actual float values
    modified_dataframe = modified_dataframe.applymap(lambda x: float(x) if isinstance(x, str) and re.match(r'^-?\d+\.\d+$', x) else x)
    
    # Replace any remaining non-numeric values with NaN
    modified_dataframe = modified_dataframe.applymap(lambda x: np.nan if not isinstance(x, (float, int)) else x)
    
    return modified_dataframe