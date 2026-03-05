
import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    # Define the pattern for brackets
    pattern = r'[(){}[\]]'
    
    # Initialize a counter for the number of brackets
    bracket_count = 0
    
    # Iterate over all elements in the DataFrame
    for col in df.columns:
        if df[col].dtype == 'object':
            bracket_count += len(re.findall(pattern, df[col].astype(str)))
    
    return bracket_count