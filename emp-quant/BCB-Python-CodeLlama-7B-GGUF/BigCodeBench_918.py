
import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    # Create a regular expression pattern to match acronyms
    pattern = r'\b(' + '|'.join(mapping.keys()) + r')\b'

    # Create a dictionary to map acronyms to their full words
    mapping_dict = {key: value for key, value in mapping.items()}

    # Apply the regular expression pattern to each string cell in the DataFrame
    for col in data.columns:
        data[col] = data[col].str.replace(pattern, lambda x: mapping_dict[x.group()])

    return data

# Replace acronyms in the DataFrame
result = task_func(data, mapping)

# Print the result
print(result)