
import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    pattern = r'[(){}[\]]'
    bracket_count = 0
    
    for column in df.columns:
        for value in df[column]:
            if isinstance(value, str):
                bracket_count += len(re.findall(pattern, value))
    
    return bracket_count