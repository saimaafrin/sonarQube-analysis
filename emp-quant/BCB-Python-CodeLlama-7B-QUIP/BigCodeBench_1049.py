
import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    # Remove empty lines and replace tabs with spaces
    non_empty_lines = [line for line in input_string.split("\n") if line.strip() != ""]
    cleaned_lines = [re.sub("\t", " ", line) for line in non_empty_lines]
    # Create a DataFrame with a single column named 'Text'
    df = pd.DataFrame({"Text": cleaned_lines})
    return df