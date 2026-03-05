
import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    """
    Process a multi-line string by replacing tabs with spaces and converting it into a pandas DataFrame.
    Each non-empty line of the input string is transformed into a separate row in the DataFrame.
    The function specifically filters out empty lines and replaces tabs with single spaces in the remaining lines.
    """
    # Split the input string into individual lines
    lines = input_string.splitlines()

    # Filter out empty lines and replace tabs with spaces
    lines = [re.sub(r'\t', ' ', line).strip() for line in lines if line.strip()]

    # Create a DataFrame with a single column named 'Text'
    df = pd.DataFrame(lines, columns=['Text'])

    return df