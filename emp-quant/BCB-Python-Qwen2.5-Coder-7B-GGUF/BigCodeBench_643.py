
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
    data_pattern (str): The regex pattern to search for in each cell.
    
    Returns:
    pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    """
    # Define a function to extract the numeric value from a string
    def extract_number(match):
        return float(match.group(0)[1:-1])
    
    # Apply the regex pattern to each element in the DataFrame
    modified_df = dataframe.applymap(lambda x: re.sub(data_pattern, lambda m: str(extract_number(m)), str(x)) if isinstance(x, str) else x)
    
    # Convert the modified DataFrame to numeric, coercing errors to NaN
    modified_df = pd.to_numeric(modified_df, errors='coerce')
    
    return modified_df

    # Apply the function
    result_df = task_func(df)
    
    # Print the result
    print(result_df)