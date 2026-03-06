
import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    # Replace tabs with spaces and filter out empty lines
    cleaned_string = re.sub(r'\t', ' ', input_string)
    cleaned_string = re.sub(r'^\s*$', '', cleaned_string)

    # Split the string into rows and create a DataFrame
    rows = cleaned_string.split('\n')
    df = pd.DataFrame({'Text': rows})

    return df