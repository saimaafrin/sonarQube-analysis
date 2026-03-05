import json
import re
import pandas as pd
def task_func(json_str):
    # Check if the input JSON string is empty
    if not json_str:
        return pd.DataFrame()
    
    # Load the JSON string into a dictionary
    data_dict = json.loads(json_str)
    
    # Function to double numerical values
    def double_values(value):
        if isinstance(value, list):
            return [double_values(x) for x in value]
        elif isinstance(value, str):
            # Try to convert string to float and double it
            try:
                return float(value) * 2
            except ValueError:
                return value
        elif isinstance(value, (int, float)):
            return value * 2
        else:
            return value
    
    # Normalize the dictionary by doubling the numerical values
    normalized_dict = {key: double_values(value) for key, value in data_dict.items()}
    
    # Create a Pandas DataFrame from the normalized dictionary
    df = pd.DataFrame(normalized_dict)
    
    return df