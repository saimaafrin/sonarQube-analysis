
import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    # Split the input string into lines
    lines = input_string.split('\n')
    
    # Filter out empty lines and replace tabs with spaces
    filtered_lines = [re.sub(r'\t', ' ', line) for line in lines if line.strip()]
    
    # Create a DataFrame with a single column 'Text'
    df = pd.DataFrame(filtered_lines, columns=['Text'])
    
    return df