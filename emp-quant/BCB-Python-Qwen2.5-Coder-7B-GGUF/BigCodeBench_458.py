
import json
import re
import pandas as pd

def task_func(json_str):
    # Check if the input JSON string is empty
    if not json_str:
        return pd.DataFrame()
    
    # Load the JSON string into a dictionary
    try:
        data_dict = json.loads(json_str)
    except json.JSONDecodeError:
        return pd.DataFrame()
    
    # Function to double numerical values
    def double_values(value):
        if isinstance(value, list):
            return [double_values(x) for x in value]
        elif isinstance(value, str):
            try:
                # Extract numbers from the string and double them
                numbers = re.findall(r'\d+', value)
                return [float(x) * 2 for x in numbers]
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