
import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    pattern = r'[(){}[\]]'
    total_brackets = 0
    
    for column in df.columns:
        if df[column].dtype == 'object':
            total_brackets += sum(len(re.findall(pattern, str(value))) for value in df[column])
    
    return total_brackets