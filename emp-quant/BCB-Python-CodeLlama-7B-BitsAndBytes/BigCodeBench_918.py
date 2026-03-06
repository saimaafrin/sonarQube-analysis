
import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    # Create a regular expression pattern to match acronyms
    pattern = re.compile(r'\b(' + '|'.join(mapping.keys()) + r')\b')

    # Create a new DataFrame with the same columns as the input DataFrame
    output = pd.DataFrame(index=data.index, columns=data.columns)

    # Iterate over each row in the input DataFrame
    for i, row in data.iterrows():
        # Iterate over each column in the input DataFrame
        for j, cell in row.iteritems():
            # If the cell is a string, replace any acronyms with their full words
            if isinstance(cell, str):
                output.at[i, j] = pattern.sub(lambda m: mapping[m.group()], cell)
            else:
                output.at[i, j] = cell

    return output